# -*- coding: UTF-8 -*-
import sys,getopt
import os


from PIL import Image

pallete_color_all = []

def rgb_hex565(red, green, blue):
    c = int((red>>3)<<11) + int((green>>2)<<5) + int(blue>>3)
    #print("0x%0.4X" % ((int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))))
    #return (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))
    return c

def bmp_process(path):
    img =Image.open(path)
    #print(img.mode)
    #print(img.size)
    #print(img.getpixel((0,26)))
    print(img.getcolors())
    print(img.getpalette())
    colors = img.getcolors()
    palette = img.getpalette()
    color_indexes = []
    for c in colors:
        if c[1] not in color_indexes:
            color_indexes.append(c[1])
    print(color_indexes)
    color_pallete = []
    for index in color_indexes:
        color_pallete.append((palette[index*3],palette[index*3+1],palette[index*3+2]))
    print(color_pallete)
    rgb_colors = []
    for index in color_pallete:
        rgb_colors.append(index[0]*255*255+index[1]*255+index[2])
    colors_16bit = []
    for c in color_pallete:
        colors_16bit.append(rgb_hex565(c[0],c[1],c[2]))
    print(colors_16bit)
    for i in colors_16bit:
        #print("0x%0.2X,0x%0.2X" % (int(i>>8), int(i & 0x00FF)))
        print("0x%0.4X, " % (int(i>>8) + int((i & 0x00FF)<<8)), end="")

    print("")

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if ((y*img.size[0] + x) > 0) and ((y*img.size[0] + x)%8 == 0):
                i = img.getpixel((x,y))
                #print("0x%0.2X,0x%0.2X", ((colors_16bit[i] & 0x00FF), colors_16bit[i]>>8))
            #else:
            #    print("")

def getPalletes(file):
    print("check " + file)
    img = Image.open(file)
    colors = img.getcolors()
    palette = img.getpalette()
    color_indexes = []
    for c in colors:
        if c[1] not in color_indexes:
            color_indexes.append(c[1])
    color_pallete = []
    for index in color_indexes:
        color_pallete.append((palette[index*3],palette[index*3+1],palette[index*3+2]))
    rgb_colors = []
    for index in color_pallete:
        rgb_colors.append(index[0] * 255 * 255 + index[1] * 255 + index[2])
    colors_16bit = []
    for c in color_pallete:
        colors_16bit.append(rgb_hex565(c[0], c[1], c[2]))
    for c in colors_16bit:
        if c not in pallete_color_all:
            pallete_color_all.append(c)

def walkFile(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            getPalletes(os.path.join(root, f))

    print(pallete_color_all)
    print("pallete size %d" % (len(pallete_color_all)))

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        file_path = sys.argv[1]
        #bmp_process(file_path)
        walkFile(file_path)