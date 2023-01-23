#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 00:21:31 2023

@author: danang
"""
'''
from PIL import Image

back = Image.open('/media/danang/E0EC3CDFEC3CB1A0/sepatu/bnib/ERA QUILTED BANDANA/DSCF2531.JPG_sh.png').resize((1080,1080))
fore = Image.open('/media/danang/E0EC3CDFEC3CB1A0/sepatu/bc.png').resize((1080,1080))

back.paste(fore, (0,0),fore.convert('RGBA'))
back.show()
'''
from glob import glob
from PIL import Image

folder = glob("/media/danang/E0EC3CDFEC3CB1A0/sepatu/bnib/*/", recursive = True)
for i in folder:
    file = glob(i+'*.png')
    for j in file:
        image = Image.open(j).resize((1080,1080))
        print(f"Original size : {image.size}") # 5464x3640
        
        templ = Image.open('/media/danang/E0EC3CDFEC3CB1A0/sepatu/bc.png').resize((1080,1080))
        image.paste(templ, (0,0), templ.convert('RGBA'))
        image.save(str(j) + '_bc.png')