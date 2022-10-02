from diffusers import StableDiffusionPipeline
from os.path import exists

pipe = StableDiffusionPipeline.from_pretrained(
  "CompVis/stable-diffusion-v1-4",
  use_auth_token=True,
)

pipe = pipe.to("mps")

salt = "Abstract art with the following vibe: "

def _gen(prompt):
  return pipe(prompt).images[0]

def generate_images(prompts):
  """Return list of filenames

  Args:
      prompts (_type_): _description_

  Returns:
      _type_: _description_
  """
  result = []
  for prompt in prompts:
    filename = f"{abs(hash(prompt))}.png"
    result.append(filename)
    if not exists(filename):
      img = _gen(salt + prompt)
      img.save(filename)
  
  return result


