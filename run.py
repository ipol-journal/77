#!/usr/bin/env python3

import subprocess
import argparse
from PIL import Image
import cv2

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--s", type=int)
ap.add_argument("--k", type=int)
ap.add_argument("--t", type=int)
args = ap.parse_args()

#convert input image into pgm
files = ["input_0", "input_1"]
for file in files:
    im = cv2.imread(file+".png")
    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(file+"pgm",img)

p = subprocess.run(['two_photos_psf_estim', '-s', str(args.s), '-k', str(args.k), '-t', str(args.t),
                    '-d', 'ipol',
                    '-o', 'psf_kernel.pgm', '-i', 'int_kernel.pgm', 'input_0.pgm', 'input_1.pgm', 
                    'psf_kernel.txt', 'int_kernel.txt'])
        
im = Image.open("psf_kernel.pgm")
# re adjust width and height to avoid visualization interpolation
width = 600
height = 600
# interpolate it by neareset neighbor
im = im.resize((width, height)) 
im.save("psf_kernel.png")

im = Image.open("int_kernel.pgm")
# re adjust width and height to avoid visualization interpolation
width = 600
height = 600
# interpolate it by neareset neighbor
im = im.resize((width, height)) 
im.save("int_kernel.png")
# convert images from .pgm to .png
im = Image.open("ipol_imgC.pgm")
im.save("ipol_imgC.png")

im = Image.open("ipol_imgW.pgm")
im.save("ipol_imgW.png")

im = Image.open("ipol_diff.pgm")
im.save("ipol_diff.png")	

im = Image.open("ipol_mask.pgm")
im.save("ipol_mask.png")