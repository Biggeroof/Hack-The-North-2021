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
base = len(imageArray[0])
height = len(imageArray)

startX, startY, endX, endY = 160, 170, 400, 400 
sequence =  algorithmSearch.search(imageArray, startX,startY, endX, endY)
print(sequence)

#creating a new image
# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros((height, base, 3), dtype=np.uint8)


for i in range(height-1):
    for j in range(base-1):
        if(imageArray[i][j] == 0):
            data[i][j] = [0,0,0]
        else:
            data[i][j] = [255,255,255]

currX, currY = startX, startY 

for i in range (len(sequence)):
    data[currY][currX] = [255, 0, 0]
    if(sequence[i] == 'D'):
        currY = currY + 1;
    elif(sequence[i] == 'R'):
        currX = currX + 1;
    elif(sequence[i] == 'U'):
        currY = currY-1;
    elif(sequence[i] == 'L'):
        currX = currX-1;
    
    
# data[512, 511] = [255, 0, 0]
# data[512, 512] = [0, 255, 0]
# data[512, 513] = [0, 0, 255]


image = Image.fromarray(data)
image.show()