from moviepy.editor import concatenate_videoclips, ImageClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import Image

def create_video(subtitles, image_paths):
  image_clips = [ImageClip(x) for x in image_paths]
  image_clips_dur = []
  for (start, end, _), ic in zip(subtitles, image_clips):
    mins, secs= divmod(end - start, 60)
    mins = int(mins)
    image_clips_dur.append(ic.set_duration(f"00:0{mins}:{secs:.2f}"))
  vid = concatenate_videoclips(image_clips_dur)

  gen = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=24, color='white')
  sub = SubtitlesClip("song.mp4.en.srt", gen)

  vid = CompositeVideoClip([vid, sub])

  aud = AudioFileClip("song.mp3")
  vid = vid.set_audio(aud)
  vid.write_videofile("final_video.mp4")
  return "final_video.mp4"