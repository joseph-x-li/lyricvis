import gradio as gr
from app import dl, vid, model

def visualize(URL):
  dl.download_song(URL)
  subtitles = dl.parse_subtitle()

  image_paths = model.generate_images(subtitles)
  vid_path = vid.create_video(subtitles, image_paths)
  return vid_path

gr.Interface(
  fn=visualize, 
  inputs="text", 
  outputs="video",
).launch()