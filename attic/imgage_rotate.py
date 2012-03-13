#rotate an image coutner clockwise (use negative degrees for clockwise?)

import Image

img = Image.open("bitter.jpg")

#roated image = source image rotated
img2 = img.rotate(90)

img2.show()

img2.save("bitter-rotated.jpg")
