# Open4K Upscaler - Google Colab Setup

import os


print("🚀 Starting Open4K AI Upscaler Setup")


# Clone repository

if not os.path.exists("Open4K-Upscaler-starter"):
    !git clone YOUR_GITHUB_REPO_URL



# Install dependencies

!pip install -U pip

!pip install \
torch \
torchvision \
opencv-python \
basicsr \
facexlib \
gfpgan \
realesrgan \
gradio



# Install FFmpeg

!apt update

!apt install ffmpeg -y



# Check GPU

import torch

if torch.cuda.is_available():

    print(
        "✅ GPU Available:",
        torch.cuda.get_device_name(0)
    )

else:

    print(
        "⚠️ GPU Not Available"
    )



# Download Real-ESRGAN model

os.makedirs(
    "models",
    exist_ok=True
)


print(
    """
Setup Complete

Next:
1. Upload video
2. Run app/main.py
3. Get 4K output
"""
)
