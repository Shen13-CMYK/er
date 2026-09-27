from PIL import Image
import matplotlib.pyplot as plt

def flip_image_lr(image_path):
    # 第一步：读取图片
    img = Image.open(image_path)
    return img