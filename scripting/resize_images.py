from PIL import Image

img = Image.open('./pics/astronaut.jpg')
img.thumbnail((400, 200))
img.save('thumbnail.jpg')
