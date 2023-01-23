# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from glob import glob
from PIL import Image

folder = glob("/media/danang/E0EC3CDFEC3CB1A0/sepatu/bnib/*/", recursive = True)
for i in folder:
    file = glob(i+'*.JPG')
    for j in file:
        image = Image.open(j)
        print(f"Original size : {image.size}") # 5464x3640
        
        sunset_resized = image.resize((1080, 1080))
        sunset_resized.save(str(j)+'_sh.png')