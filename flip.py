from PIL import Image
import matplotlib.pyplot as plt

def flip_image_lr(image_path):
    # 读取图片
    img = Image.open(image_path)
    # 左右翻转
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    # 并排显示原图和翻转后的图
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title('Original')
    axes[0].axis('off')
    axes[1].imshow(flipped)
    axes[1].set_title('Flipped Left-Right')
    axes[1].axis('off')
    plt.show()
    return flipped