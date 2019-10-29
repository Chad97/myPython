import tesserocr

from PIL import Image
image = Image.open('img.png')

print(tesserocr.image_to_text(image))