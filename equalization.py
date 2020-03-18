import cv2

image = cv2.imread('yahya.jpg')
img_shape  = img.shape
height = img_shape[0]
width = img_shape[1]

for row in range(width):
    for column in range(height):
        print(image[column][row])