from PIL import Image

# returns Image object
img = Image.open('ScottyTheBear.png') 

# prints out image's format, size, and color value
print(img.format, img.size, img.mode)
img.show()
