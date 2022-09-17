from PIL import Image
import pytesseract
import numpy as np


filename = input('Please add the name of the file you would like the script to scan: ')
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)
