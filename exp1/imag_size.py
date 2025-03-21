from PIL import Image

# 打开图像
img = Image.open(r"blueyellow/f1_blueyellow.png")

# 获取图像大小
width, height = img.size
print(f"图像宽度: {width}, 图像高度: {height}")

