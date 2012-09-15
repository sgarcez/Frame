#!/usr/bin/env python

__author__ = 'Sergio Garcez'

import sys, re, time
from PIL import Image, ImageEnhance, ImageDraw

# Device comp builder
#
# 

class Comp:
    def __init__(self, user_img, overlay_img, user_img_offset=(0,0),  background='white'):
        self.user_img = Image.open(user_img)
        self.user_img_offset = user_img_offset
        self.overlay_img = Image.open(overlay_img)
        self.background_colour = background

    def reduce_opacity(self, im, opacity):
        """returns an image with reduced opacity"""
        assert opacity >= 0 and opacity <= 1
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        else:
            im = im.copy()
        alpha = im.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        im.putalpha(alpha)
        return im


    def build(self):
        """composites an image"""
        background = Image.new('RGBA', self.overlay_img.size, (0,0,0,0))
        draw = ImageDraw.Draw(background)
        draw.rectangle((0,0)+self.overlay_img.size, fill=self.background_colour)
            
        self.user_img_layer = Image.new('RGBA', self.overlay_img.size, (0,0,0,0))
        self.user_img_layer.paste(self.user_img, self.user_img_offset)
        
        self.user_img_layer = Image.composite(self.user_img_layer, background, self.user_img_layer)
        
        if self.overlay_img.mode != 'RGBA':
            self.overlay_img = self.overlay_img.convert('RGBA')

        return Image.composite(self.overlay_img, self.user_img_layer, self.overlay_img)
    

def main():
    from optparse import OptionParser
    parser = OptionParser(usage='usage: %prog [options] arguments')
    parser.add_option("-i", "--image",
                      dest="user_image", default=None,
                      help="user image")
    parser.add_option("-f", "--offset",
                      dest="offset", default= '0,0',
                      help="user image offset")
    parser.add_option("-o", "--overlay",
                      dest="overlay_image", default='glare-iPhone-4s-white.png',
                      help="overlay image")
    parser.add_option("-b", "--background",
                      dest="background", default='white',
                      help="background colour")

    (options, args) = parser.parse_args()
 
    
    if not options.user_image:
        parser.error('Image filename not given')
    if not options.overlay_image:
        parser.error('overlay filename not given')
    if options.offset:
        options.offset = tuple(map(int, options.offset.split(',')))
        
        
    c = Comp(options.user_image, options.overlay_image, options.offset, options.background)
    comp = c.build()
    comp.show()
    comp.save('output/output_' + str(time.time()) + '.jpg')

if __name__ == '__main__':
    main()