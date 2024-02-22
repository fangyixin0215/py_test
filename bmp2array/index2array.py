import sys,getopt
import os
import getpass # For getpass.getuser()
from tkinter.tix import Tree
from PIL import Image
user = getpass.getuser()
path = 'C:/Users/%s/Desktop/bmp_array.txt'%(user) # Get file path
fp = open("path", "a+") # Open file

total_size = 0

INDEX_TYPE_INVALID = 0
INDEX_TYPE_16 = 1
INDEX_TYPE_32 = 2
INDEX_TYPE_64 = 3
INDEX_TYPE_128 = 4
INDEX_TYPE_256 = 5

def rgb_hex565(red, green, blue):
    c = int((red>>3)<<11) + int((green>>2)<<5) + int(blue>>3)
    #print("0x%0.4X" % ((int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))))
    #return (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))
    return c

def parseImage(file, name):
    print("ParseImage %s" % (file), file = fp)
    cur_palette = []
    output = []
    output2 = []
    # 使用Image库打开图片
    img = Image.open(file)
    # 检查是否为索引图
    if img.mode == 'P':
        # 将图片宽高存入图片索引数组
        s = img.size
        output.append(s[0])
        output.append(s[1])
        global total_size
        total_size = total_size + (s[0]*s[1])
        # 获取图片索引分布
        index_used_in_palette = img.getcolors()
        index_count = len(index_used_in_palette)
        index_type = INDEX_TYPE_INVALID

        if index_count > 256:
            return
        elif index_count > 16:
            index_type = INDEX_TYPE_256
        else:
            index_type = INDEX_TYPE_16

        # 获取图片索引色盘
        palette_in_img = img.getpalette()

        for s in index_used_in_palette:
            index_num = s[1]
            c = rgb_hex565(palette_in_img[index_num*3], palette_in_img[index_num*3 + 1], palette_in_img[index_num*3 + 2])
            if c not in cur_palette:
                cur_palette.append(c)

        print("[%d] = {" % (len(cur_palette)),file = fp)
        count = 0
        for i in cur_palette:
            if cur_palette.index(i) == (len(cur_palette) - 1):
                print("0x%0.4X" % (int(i>>8) + int((i & 0x00FF)<<8)), end="", file = fp)
            else:
                print("0x%0.4X, " % (int(i >> 8) + int((i & 0x00FF) << 8)), end="", file = fp)
            count = count + 1
            if count == 16:
                print("", file = fp)
                count = 0
        print("", file = fp)
        print("};", file = fp)
        print("", file = fp)

        # 初始化索引点
        if index_type == INDEX_TYPE_16:
            for i in range(int((img.size[0] * img.size[1] + 1) / 2)):
                output.append(0)
        elif index_type == INDEX_TYPE_256:
            for i in range(img.size[0] * img.size[1]):
                output.append(0)

        # 遍历图片像素点
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                p = img.getpixel((x,y))
                c = rgb_hex565(palette_in_img[p*3], palette_in_img[p*3 + 1], palette_in_img[p*3 + 2])
                curr_pixel_position = y*img.size[0] + x
                index = cur_palette.index(c)

                if index_type == INDEX_TYPE_16:
                    output_index = int(curr_pixel_position / 2)
                    if curr_pixel_position % 2 == 0:
                        output[output_index + 2] = output[output_index + 2] + (index<<4)
                    else:
                        output[output_index + 2] = output[output_index + 2] + index
                elif index_type == INDEX_TYPE_256:
                    output[curr_pixel_position + 2] = index

        # print("const unsigned char menu_stopwatch_slice_%d[%d] = {" % (int(name), len(output)))
        print("[%d] = {" % (len(output)),file = fp)
        print("%d, %d," % (output[0], output[1]), file = fp)

        count = 0
        for i in range(2, len(output)):
            if (i == (len(output) - 1)):
                print("0x%0.2X" % (output[i]), end="",file = fp)
            else:
                print("0x%0.2X," % (output[i]), end="", file = fp)
            count = count + 1
            if (count == 16 and i != (len(output) - 1)):
                print("",file = fp)
                count = 0
        print("",file = fp)
        print("};",file = fp)
        print("", file = fp)
    else:
        print("Error: Not indexed BMP file %s" % (file), file = fp)

def walkFile(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            name,_ = f.split('.')
            parseImage(os.path.join(root, f), name)

if __name__ == "__main__":
    # 遍历图片文件夹
    if (len(sys.argv) == 2):
        file_path = sys.argv[1]
        walkFile(file_path)
        print("total_size %d" % (total_size/2))
    else:
        print("Usage sample: Python index2array.py folder/to/image")
        # for i in range(0, 94):
        #     print("\t// %c" % (i+33))
        #     print("\timg_alphabet_font_group.img[i].img_ptr = (uint8_t*)font_%d;" % (i+33))
        #     print("\timg_alphabet_font_group.img[i].baseline =");
        #     print("\ti++;")
        #     print("")