# HEIF to PNG Converter
# usage: upload heif images to "heif" director
# run using python heif-png.py
# change some lines for other extensions

from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

path = "heif"
for name in os.listdir(path):
    filepath = os.path.join(path, name)
    im = Image.open(filepath)
    im.save(f"png/{name}.png")
