from PIL import Image, ImageEnhance, ImageFilter
import os
path = './imgs'
for filename in os.listdir(path):
    img = Image.open(f"{path} / {filename}")
    