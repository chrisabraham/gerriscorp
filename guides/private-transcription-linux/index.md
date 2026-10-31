> Turn client calls and meeting recordings into searchable transcripts offline with ffmpeg and Whisper, speaker labels included, on hardware you already own.
>
> Source: https://gerriscorp.com/guides/private-transcription-linux/ · Updated 2026-10-31 · By Chris Abraham, Gerris Corp

# How to transcribe recordings privately on your own Linux machine

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 31, 2026

Cloud transcription services all ask for the same thing: your recording, on their servers. Client calls, interviews, and internal meetings carry material with no reason to leave your building. Two free command line tools, ffmpeg and Whisper, produce a written transcript entirely offline on ordinary Linux hardware, with speaker labels when you need them. I run this on a ThinkPad W520 from 2011, and it finishes an hour of talk in about thirty minutes.

## What you need
- A Linux machine. The commands here are for Linux Mint, Ubuntu, and Debian.
- A 64 bit processor. A graphics card speeds things up and is optional. On my run the small model held about 1.7 GB of memory.
- About a gigabyte of disk for the model, plus a few more if you add speaker labels.
- An internet connection once, for the model download. After that, nothing leaves the machine.

## Install the tools

```
sudo apt install ffmpeg pipx
pipx ensurepath
```

Open a new terminal so the updated path loads, then install the transcriber:

```
pipx install whisper-ctranslate2
```

[whisper-ctranslate2](https://github.com/Softcatala/whisper-ctranslate2) is a command line front end for [faster-whisper](https://github.com/SYSTRAN/faster-whisper). It takes the same arguments as OpenAI's original Whisper program and runs up to four times faster on a CPU at equal accuracy. pipx gives it a private environment, so it never disturbs the Python your operating system relies on.

## Reduce the recording to speech

Whisper hears every file as a single channel at 16 kHz, so converting to exactly that before transcribing loses nothing and saves a great deal of disk and transfer:

```
ffmpeg -i "meeting.mp4" -vn -ac 1 -ar 16000 -c:a libopus -b:a 24k -application voip "meeting.opus"
```

The flags remove the picture, mix to mono, set the sample rate, and encode with Opus tuned for voices. An hour lands near 11 MB; my 5.9 GB screen recording shrank by more than 99 percent. Whisper also reads video directly, but the small audio file is quicker to move, back up, and keep.

## Transcribe it

```
whisper-ctranslate2 "meeting.opus" --model small --language en --output_format txt
```

The first run fetches the model from Hugging Face and prints a warning about unauthenticated requests, which you can ignore. After that it stays silent until it finishes and writes `meeting.txt` next to the audio. Add `--verbose True` to watch lines arrive with their timestamps.

Other formats are one flag away:
- `--output_format srt` or `vtt` produces timed captions for a video editor or player.
- `--output_format json` produces word timings and confidence scores for scripts.
- `--output_format all` writes every format in one pass.

## Choose a model
- `tiny` and `base` are quick and stumble on names, jargon, and quiet voices.
- `small` is my default on a laptop processor. It kept names and crosstalk intact on my recordings.
- `medium` is clearly more accurate and several times slower. Start it before lunch.
- `large-v3` is the most accurate and belongs on a machine with a capable graphics card.

Pass `--language en` whenever you know the language. Without it, Whisper guesses from the opening thirty seconds, and a wrong guess spoils the entire transcript.

## Speed it up on older hardware

```
nice -n 19 whisper-ctranslate2 "meeting.opus" --model small --language en --output_format txt --threads 8 --vad_filter True --compute_type int8
```
- `--threads 8` puts every logical core to work. Use whatever number `nproc` reports.
- `--vad_filter True` skips the silences, which shortens long recordings and stops the model from inventing text during pauses.
- `--compute_type int8` selects the quickest arithmetic on a CPU.
- `nice -n 19` runs the job at the lowest priority, so the computer stays responsive while you keep working.

## Label the speakers

Speaker labels come from [pyannote.audio](https://github.com/pyannote/pyannote-audio), which also runs locally. Its models sit behind a free Hugging Face account.
1. Create a free account at [Hugging Face](https://huggingface.co/).
2. Create a token with read access on the [access tokens page](https://huggingface.co/settings/tokens). It is shown once, so copy it right away.
3. While signed in, accept the terms on [pyannote/speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1). Older releases of whisper-ctranslate2 use [speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1) and [segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0), so accept those too. Each page asks for a company name and a website before it unlocks; use your organization's name and address.
4. Add pyannote.audio to the transcriber's environment and store the token in your shell profile:

```
pipx inject whisper-ctranslate2 pyannote.audio
echo 'export HF_TOKEN=hf_yourtokenhere' >> ~/.bashrc
source ~/.bashrc
```

Then pass the token with each run:

```
whisper-ctranslate2 "meeting.opus" --model small --language en --output_format txt --hf_token "$HF_TOKEN"
```

Every line comes back tagged `[SPEAKER_00]`, `[SPEAKER_01]`, and onward. The install brings in PyTorch, which is over a gigabyte, and labeling is a second complete pass over the audio, so a run takes roughly twice as long. The token only authorizes the model download; the audio itself stays on the machine. Keep the token out of shared scripts and code repositories.

## Make it a routine

Two functions at the end of `~/.bashrc` reduce the job to two short commands:

```
toaudio() { ffmpeg -i "$1" -vn -ac 1 -ar 16000 -c:a libopus -b:a 24k -application voip "${1%.*}.opus"; }
transcribe() { nice -n 19 whisper-ctranslate2 "$1" --model small --language en --output_format txt --vad_filter True --threads 8 --output_dir ~/Documents/Transcripts --hf_token "$HF_TOKEN"; }
```

After running `source ~/.bashrc` once, each recording takes:

```
toaudio "meeting.mp4"
transcribe "meeting.opus"
```

To work through a folder of recordings overnight:

```
for f in ~/Recordings/*.mp4; do
  toaudio "$f" && transcribe "${f%.*}.opus"
done
```

`--output_dir` gathers every transcript in one folder. When that folder syncs between your own computers with a tool like Syncthing, every transcript follows you without touching a third party's cloud. Searching all of them is a single line:

```
grep -ril "renewal" ~/Documents/Transcripts
```

Drop the `-l` to print the matching lines themselves.

## Troubleshooting
- **"command not found" for whisper-ctranslate2.** Run `pipx ensurepath` and open a new terminal.
- **A warning about unauthenticated requests to the HF Hub.** Harmless. Setting `HF_TOKEN` silences it.
- **A 401, 403, or gated repository error while labeling speakers.** Accept the model terms while signed in to the same account that issued the token.
- **One sentence repeated again and again.** That is Whisper filling silence. Add `--vad_filter True`.
- **A transcript in the wrong language, or translated.** Set `--language` explicitly.
- **Too slow.** Drop one model size, set `--threads` to your core count, and leave speaker labels off for recordings that don't need them.

Setting up private tools like this for a team is part of my [AI tools and automation](https://gerriscorp.com/services/ai-automation/) work.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [whisper-ctranslate2 on GitHub](https://github.com/Softcatala/whisper-ctranslate2)
- [faster-whisper on GitHub](https://github.com/SYSTRAN/faster-whisper)
- [OpenAI Whisper on GitHub](https://github.com/openai/whisper)
- [pyannote.audio on GitHub](https://github.com/pyannote/pyannote-audio)
- [FFmpeg codecs documentation](https://ffmpeg.org/ffmpeg-codecs.html)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)
