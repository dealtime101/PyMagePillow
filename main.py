from PIL import Image

#Create an image via import
image = Image.open('cat.jpg')

# analyze the image
print(image.size)
print(image.filename)
print(image.format)

# flip the image
#image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
#image = image.transpose(Image.Transpose.ROTATE_90)

#exercise
cat_rotated = image.rotate(30)
cat_rotated.save('cat_rotated.png', 'png')

#show the image
image.show()
