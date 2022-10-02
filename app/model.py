from diffusers import StableDiffusionPipeline
from os.path import exists
# pipe = StableDiffusionPipeline.from_pretrained("/Users/josephli/Github/lyricvis/app/stable-diffusion-v1-4")
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_api_key=True)

pipe = pipe.to("mps")

salt = "Realistic, modern, concept art, HQ, image with the following caption: "

def _gen(prompt):
  return pipe(prompt).images[0]

def generate_images(prompts):
  """Return list of filenames
  """
  result = []
  prompts_shift = [None] + prompts[:-1]
  for p_back, prompt in zip(prompts_shift, prompts):
    filename = f"{abs(hash(prompt))}.png"
    result.append(filename)
    if not exists(filename):
      print(f"Generating on")
      full_prompt = salt + p_back + prompt
      print(f"full_prompt")
      print(f"...")
      img = _gen(full_prompt)
      img.save(filename)
  
  return result


