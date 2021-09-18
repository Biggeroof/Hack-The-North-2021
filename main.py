from PIL import Image
import sys
#import pygame
import math
import algorithmSearch
import numpy as np
import scipy.misc as smp
from colors import *
from queue import PriorityQueue
np.set_printoptions(threshold=sys.maxsize)
floorPlanImage = Image.open("floorPlan.jpeg")
fn = lambda x : 255 if x > 200 else 0
base, height = 0,0
#convert the image to pure black-white and save it as foo.png
r = floorPlanImage.convert('L').point(fn, mode='1')
r.save('foo.png')
import test

#Turn the foo.png into a workable 2D array
#it seems like '1' means white square, and '0' means black
imageArray = np.array(r, dtype=np.uint8)

#traverse graph?
imageArray[0][0] = -1
imageArray[537][760] = -2
n_cols = len(imageArray[0])
n_rows = len(imageArray)

start_row, start_col, end_row, end_col = 160, 170, 400, 400 
sequence =  algorithmSearch.search(imageArray, start_row, start_col, end_row, end_col)
print(sequence)

#creating a new image
# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros((n_rows, n_cols, 3), dtype=np.uint8)


for row in range(n_rows):
    for col in range(n_cols):
        if(imageArray[row][col] == 0):
            data[row][col] = [0,0,0]
        else:
            data[row][col] = [255,255,255]

curr_row, curr_col = start_row, start_col

for i in range (len(sequence)):
    data[curr_row][curr_col] = [255, 0, 0]
    if(sequence[i] == 'D'):
        curr_row = curr_row - 1;
    elif(sequence[i] == 'R'):
        curr_col = curr_col + 1;
    elif(sequence[i] == 'U'):
        curr_row = curr_row +1;
    elif(sequence[i] == 'L'):
        curr_col = curr_col -1;
    
    
# data[512, 511] = [255, 0, 0]
# data[512, 512] = [0, 255, 0]
# data[512, 513] = [0, 0, 255]


image = Image.fromarray(data)
image.show()
image.save("drawn.png")
