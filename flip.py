from PIL import Image, ImageDraw
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

# 自动生成一张测试图片
def make_test_image():
    img = Image.new('RGB', (400, 300), 'white')
    d = ImageDraw.Draw(img)
    d.polygon([(80, 150), (250, 150), (250, 100), (350, 150), (250, 200), (250, 150)], fill='red')
    d.text((160, 250), 'Before', fill='black')
    img.save('test.jpg')

if __name__ == '__main__':
    make_test_image()
    flip_image_lr('test.jpg')