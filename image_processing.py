import numpy as np
import cv2
from collections import Counter

file_img_path = 'image/image-s.png'
img = cv2.imread(file_img_path)
# get size image 

image_size = img.shape
# with x height
image_size_w = image_size[0] 
image_size_h = image_size[1] 
#array get color from image
Arr_screen_color = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

hex_code_unique = []
hex_code_sum_color = []

for tuple_rgb in Arr_screen_color:
    for rgb_code in tuple_rgb:
        # convert rgb to hex code
        code_hex =  '#{:02x}{:02x}{:02x}'.format(rgb_code[0],rgb_code[1],rgb_code[2])
        hex_code_unique.append(code_hex)
        hex_code_sum_color.append(code_hex)


num_count_color = Counter(hex_code_sum_color)
print()
# unique color hex code
hex_code_unique = list(set(hex_code_unique))
# print(len(hex_code_unique))

