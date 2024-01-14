# This file runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

import torch
from diffusers import StableDiffusionPipeline

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    StableDiffusionPipeline.from_pretrained("ECRodriguez/ecrodriguez-workshop", torch_dtype=torch.float16)

if __name__ == "__main__":
    download_model()