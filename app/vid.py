from moviepy.editor import concatenate_videoclips, ImageClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import Image

def create_video(subtitles, image_paths):
  if subtitles[0][0] > 0: # start of first subtitle is not @ 00:00
    # 0 -> begin, same path
    # add a fake frame
    image_paths = [image_paths[0]] + image_paths
    subtitles = [(0.0, subtitles[0][0], subtitles[0][1])] + subtitles
  image_clips = [ImageClip(x) for x in image_paths]
  image_clips_dur = []
  for idx, (start, end, _), ic in enumerate(zip(subtitles, image_clips)):
    if idx < len(subtitles) - 1: # not at the end
      end = subtitles[idx + 1][0] # set the end as the start of the next
    mins, secs = divmod(end - start, 60)
    mins = int(mins)
    image_clips_dur.append(ic.set_duration(f"00:0{mins}:{secs:.2f}"))
  vid = concatenate_videoclips(image_clips_dur)

  gen = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=18, color='white', method="caption", size=(512, 512), align="South")
  sub = SubtitlesClip("song.mp4.en.srt", gen)

  vid = CompositeVideoClip([vid, sub])

  aud = AudioFileClip("song.mp3")
  vid = vid.set_audio(aud)
  vid.write_videofile("final_video.mp4", fps=24)
  return "final_video.mp4"
