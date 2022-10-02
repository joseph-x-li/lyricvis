import youtube_dl
import webvtt

def download_song(url):
  ydl_opts = {
    # Subtitle shit
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'song.mp4',
    # Subtitle shit
    'writesubtitles': True,
    'subtitle': '--write-sub --sub-lang en --sub-format srt',
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

def _parse_timestamp(ts):
  times = ts.split(':')
  sec = float(times[-1])
  min = int(times[-2])
  return float(min * 60) + sec

def _to_ascii(s):
  return ''.join([i if ord(i) < 128 else ' ' for i in s])

def parse_subtitle():
  filename = "song.mpt.en.vtt"
  result = []
  for caption in webvtt.read(filename):
    start = _parse_timestamp(caption.start)
    end = _parse_timestamp(caption.end)
    text = _to_ascii(caption.text)
    result.append((start, end, text))

  return result