from moviepy.editor import *

def attach_subtitles(movie, subtitles_file="song.mp4.en.vtt"):
  generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=24, color='white')
  sub = SubtitlesClip("subtitles.srt", generator)