import sys,getopt
import os
from PIL import Image

bw_pallete = [0x0000, 0xFFFF]

def rgb_hex565(red, green, blue):
    c = int((red>>3)<<11) + int((green>>2)<<5) + int(blue>>3)
    #print("0x%0.4X" % ((int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))))
    #return (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))
    return c

def parseImage(file):
    print("ParseImage %s" % (file))
    output = []
    # 使用Image库打开图片
    img = Image.open(file)
    # 检查是否为索引图
    if img.mode == 'P':
        # 将图片宽高存入图片索引数组
        s = img.size
        output.append(s[0])
        output.append(s[1])
        # 获取图片索引分布
        index_used_in_palette = img.getcolors()
        # 获取图片索引色盘
        palette_in_img = img.getpalette()

        for s in index_used_in_palette:
            index_num = s[1]
            c = rgb_hex565(palette_in_img[index_num*3], palette_in_img[index_num*3 + 1], palette_in_img[index_num*3 + 2])
            if c not in bw_pallete:
                return "Error: Not a Black White Only Image"

        # 初始化索引点
        for i in range(int(img.size[0] * img.size[1] / 2)):
            output.append(0)

        # 遍历图片像素点
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                p = img.getpixel((x,y))
                c = rgb_hex565(palette_in_img[p*3], palette_in_img[p*3 + 1], palette_in_img[p*3 + 2])
                curr_pixel_position = y*img.size[0] + x
                output_index = int(curr_pixel_position/2)
                if c == bw_pallete[1]:
                    if curr_pixel_position % 2 == 0:
                        output[output_index + 2] = output[output_index + 2] + 0x10
                    else:
                        output[output_index + 2] = output[output_index + 2] + 0x01

        print("[%d] = {" % len(output))
        print("%d, %d," % (output[0], output[1]))

        count = 0
        for i in range(2, len(output)):
            print("0x%0.2X," % (output[i]), end="")
            count = count + 1
            if (count == 16):
                print("")
                count = 0
        print("")
        print("};")
    else:
        print("Error: Not indexed BMP file %s" % (file))

def walkFile(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            parseImage(os.path.join(root, f))

if __name__ == "__main__":
    # 遍历黑白图片文件夹
    if (len(sys.argv) == 2):
        file_path = sys.argv[1]
        walkFile(file_path)