from diffusers import StableDiffusionPipeline
from os.path import exists
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_api_key=True).to("cuda")

salt = "Realistic, real, life-like, concept art, 4K, HQ, no text, image with the caption: "

def _gen(prompt):
  return pipe(prompt, num_inference_steps=50).images[0]

def generate_images(captions):
  """Return list of filenames
  """
  result = []
  captions_shift = [(None, None, None)] + captions[:-1]
  for c_back, cap in zip(captions_shift, captions):
    p_back, prompt = c_back[2], cap[2]
    filename = f"{abs(hash(prompt))}.png"
    result.append(filename)
    if not exists(filename):
      full_prompt = salt + " " + p_back + " " + prompt if p_back is not None else salt + " " + prompt
      print(f"Generating using: {full_prompt}...", end="")
      img = _gen(full_prompt)
      img.save(filename)
  
  return result


