from ultralytics import YOLO
from PIL import Image
import random

#导入模型
model = YOLO('slope_detection_yolov8n.pt')

# 生成随机数（0-1952）
for i in range(0,20):
    random_num = random.randint(0, 1952)
    im1 = Image.open("./dataset/{}.jpg".format(random_num))

    results = model.predict(source=im1, save=True)