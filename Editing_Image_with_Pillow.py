from PIL import Image

image = Image.open("nature.jpg")

width, height = image.size

box = (0, 0, width//2, height//2)
black_left_quarter = Image.new("RGB", (width//2, height//2), (0, 0, 0))

image.paste(black_left_quarter, box)
image.save("Edited_Image.jpg")