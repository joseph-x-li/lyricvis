import gradio as gr
from . import dl, vid, model



def visualize(url):
  dl.download_song(url)
  captions = dl.parse_subtitle()
  image_paths = model.generate_images(captions)
  vid_path = create_video()
  return vid_path

gr.Interface(
  fn=visualize, 
  inputs="text", 
  outputs="video",
).launch()