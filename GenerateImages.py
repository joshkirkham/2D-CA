from PIL import Image
from IPython.display import display
import random
import os

ONE = (0,0,0)
ZERO = (255,255,255)
BASE_PATH = "random/"

def func(a, b, c):

	x = 0
	if a == ONE:
		x += 1
	x <<= 1
	if b == ONE:
		x += 1
	x <<= 1
	if c == ONE:
		x += 1

	if rule & (1 << x) == 0:
		return ZERO
	return ONE


MyImg = Image.new( 'RGB', (250,250), "white") 
pixels = MyImg.load() # creates the pixel map
display(MyImg)        # displays the black image


for x in range(MyImg.size[0]):
	num = random.randint(0, 1)
	if num == 0:
		pixels[x,0] = ZERO
	elif num == 1:
		pixels[x,0] = ONE



for rule in range(0, 255):
	for row in range(1, MyImg.size[1]):
		for col in range(0, MyImg.size[0]):
			if col-1 < 0:
				pixels[col, row] = func(ZERO, pixels[col,row-1], pixels[col+1,row-1])
			elif col+1 >= MyImg.size[0]:
				pixels[col, row] = func(pixels[col-1,row-1], pixels[col,row-1], ZERO)
			else:
				pixels[col,row] = func(pixels[col-1,row-1], pixels[col,row-1], pixels[col+1,row-1])

	MyImg.save(os.path.join(BASE_PATH, str(rule) + ".png"))
	print(str(rule))
#display(MyImg)        # displays the changed colourful image
#MyImg.show()


