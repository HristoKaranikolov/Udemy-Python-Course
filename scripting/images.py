from PIL import Image, ImageFilter

img = Image.open('pics/Ichigo.jpg')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save('grey.png', 'png')

resize = filtered_img.resize((30, 30))

box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
cropped.show()
