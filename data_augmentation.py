import os
import random
import glob
from PIL import Image, ImageFilter

image_path = '.\dataset'
# 读取文件夹下所有图片
image_list = glob.glob(os.path.join(image_path, '*.jpg'))
print(image_list)
# 数据增强
for image in image_list:
    img = Image.open(image)
    if img.mode == "RGBA":
        img = img.convert('RGB')
    # 旋转
    for i in range(3):
        img_rotate = img.rotate(random.randint(0, 360))
        img_rotate.save(image[:-4] + '_rotate' + str(i) + '.jpg')
    # 翻转
    img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_flip.save(image[:-4] + '_flip.jpg')
    # 亮度
    img_enhance = Image.blend(img, img, random.uniform(0.5, 1.5))
    img_enhance.save(image[:-4] + '_enhance.jpg')
    # 对比度
    img_contrast = Image.blend(img, img_enhance, random.uniform(0.5, 1.5))
    img_contrast.save(image[:-4] + '_contrast.jpg')
    # 锐度
    img_sharp = img.filter(ImageFilter.SHARPEN)
    img_sharp.save(image[:-4] + '_sharp.jpg')
    # 模糊
    img_blur = img.filter(ImageFilter.BLUR)
    img_blur.save(image[:-4] + '_blur.jpg')

