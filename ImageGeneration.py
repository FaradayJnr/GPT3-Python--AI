#GPT-3 Image Generation
import os
import openai
openai.api_key = "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"
#Image generation
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
#image Edits
responseEdit = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url_1 = responseEdit['data'][0]['url']

#image variations
responseVariation = openai.Image.create_variation(
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url_2 = responseVariation['data'][0]['url']
