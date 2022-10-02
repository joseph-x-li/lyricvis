import gradio as gr
import dl, vid, model



def visualize(url):
  dl.download_song(url)
  subtitles = dl.parse_subtitle()
  image_paths = model.generate_images(subtitles)
  vid_path = vid.create_video(subtitles, image_paths)
  return vid_path

gr.Interface(
  fn=visualize, 
  inputs="text", 
  outputs="video",
).launch()