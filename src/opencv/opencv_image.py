import cv2

"""
    图片操作
"""

img_path = "resources/img_soa.png"
image = cv2.imread(img_path)

# 以彩色模式读取图片
image_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow("Color Image", image_color)

# 以灰度模式读取图片
image_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Grayscale Image", image_gray)


cv2.waitKey(0)  # 等待用户按键
cv2.destroyAllWindows()  # 关闭所有窗口


#########################################################################
if image is None:
    print("Error: Could not load image.")
    exit()

# 图片信息 (高, 宽, 颜色通道)
print(image.shape)
original_height, original_width = image.shape[:2]

# 计算新尺寸
new_width = int(original_width / 2)
new_height = int(original_height / 2)

# 图片缩放
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
# 图片旋转

cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)  # 等待用户按键
cv2.destroyAllWindows()  # 关闭所有窗口
