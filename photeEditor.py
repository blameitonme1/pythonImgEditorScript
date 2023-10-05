from PIL import Image, ImageEnhance, ImageFilter
import os
path = './imgs'
pathout = "/editedImgs"
for filename in os.listdir(path):
    # 注意别加空格
    img = Image.open(f"{path}/{filename}")
    # 轮廓
    edit = img.filter(ImageFilter.CONTOUR)
    # 干净的名字
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathout}/{clean_name}_edited.jpg')

