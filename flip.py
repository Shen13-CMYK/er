from PIL import Image
import matplotlib.pyplot as plt

def flip_image_lr(image_path):
    # 读取图片
    img = Image.open(image_path)
    # 左右翻转
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped