#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import colorsys
from PIL import Image, ImageEnhance

def lighting_1(finp):

    try:
        image = Image.open(finp)
    except OSError:
        print("Error! Failed to open file\n")
        return 1
    
    arr = np.asarray(image)

    shape = arr.shape


    bright = 0
    
    for i in range(shape[0]):
        for j in range(shape[1]):
             if  bright < int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2]) :
              #  print(bright)
                bright = int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2])
                R0 = int(arr[i][j][0])
                G0 = int(arr[i][j][1])
                B0 = int(arr[i][j][2])
                
   
    (H0, S0, V0) = colorsys.rgb_to_hsv(R0,G0, B0)
    dV = 255 - V0
    
    for i in range(shape[0]):
        for j in range(shape[1]): 
            (a,b,c) =  colorsys.rgb_to_hsv(int(arr[i][j][0]),int(arr[i][j][1]), int(arr[i][j][2]))
            b -= S0
            c += dV
            
            if c > 255:
                c = 255
            (arr[i][j][0],arr[i][j][1], arr[i][j][2]) = colorsys.hsv_to_rgb(a,b,c)
             #   print("ok")
             #   print(arr[i][j][0],arr[i][j][1], arr[i][j][2])
               
    pil_image = Image.fromarray(arr)
    pil_image.save('rez_1.jpeg')

def lighting_2(finp):

    try:
        image = Image.open(finp)
    except OSError:
        print("Error! Failed to open file\n")
        return 1
    
    arr = np.array(image)

    shape = arr.shape
    
    dif1 = 0
    dif2 = 0
    dif3 = 0
    bright = 0
    
    for i in range(shape[0]):
        for j in range(shape[1]):
             if  bright < int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2]) :
              #  print(bright)
                bright = int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2])
                dif1 = 256 - int(arr[i][j][0])
                dif2 = 256 - int(arr[i][j][1])
                dif3 = 256 - int(arr[i][j][2])
    
    dif = max(dif1, dif2, dif3)
    for i in range(shape[0]):
        for j in range(shape[1]):   
            if arr[i][j][0] + dif > 255:
                arr[i][j][0] = 255
            else:
                arr[i][j][0] += dif
                
            if arr[i][j][1] + dif > 255:
                arr[i][j][1] = 255
            else:
                arr[i][j][1] += dif
                
            if arr[i][j][2] + dif > 255:
                arr[i][j][2] = 255    
            else:
                arr[i][j][2] += dif
             
                
    pil_image = Image.fromarray(arr)
    pil_image.save('rez_2.jpeg')
    
def test():

    try:
        image = Image.open('rez.jpeg')
    except OSError:
        print("Error test! Failed to open file\n")
        return 1
    
    arr = np.asarray(image)

    shape = arr.shape
    
    bright = 0
    
    for i in range(shape[0]):
        for j in range(shape[1]):
             if  bright < int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2]) :
                bright = int(arr[i][j][0]) + int(arr[i][j][1]) + int(arr[i][j][2])
                R0 = int(arr[i][j][0])
                G0 = int(arr[i][j][1])
                B0 = int(arr[i][j][2])
                
    if (R0,G0,B0) != (255,255,255):
        print("oops")
        print(R0,G0,B0)
    
    

    
file = input("Enter name of file with pic\n")

lighting_1(file)
lighting_2(file)
test()
print("open rez_1.jpeg and rez_2.jpeg \n")

