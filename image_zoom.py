from PIL import Image  
  
def scale_image_with_pil(image_path, scale_factor):  
    # 打开图像  
    img = Image.open(image_path)  
      
    # 计算新的尺寸  
    new_width = int(img.width * scale_factor)  
    new_height = int(img.height * scale_factor)  
      
    # 使用ANTIALIAS（或BILINEAR, BICUBIC等，但注意Pillow的resize默认是BILINEAR）进行放大  
    # 为了更接近双三次插值，我们可以显式指定resample参数为Image.BICUBIC  
    resized_img = img.resize((new_width, new_height), Image.BICUBIC)  
      
    # 显示原图和放大后的图像（需要安装Pillow的依赖matplotlib或tkinter等）  
    # 这里为了简化，只展示保存放大后的图像  
    resized_img.save('resized_image.jpg')  
    # 如果需要显示，可以使用resized_img.show()（注意这可能需要额外的依赖）  
  
# 使用示例  
image_path = 'path_to_your_image.jpg'  # 替换为你的图片路径  
scale_factor = 2  # 放大比例  
scale_image_with_pil(image_path, scale_factor)