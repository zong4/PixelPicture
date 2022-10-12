# -*- coding : utf-8 -*-
# @Time      : 2022/6/3 19:38
# @Author    : Zong
# @File      : SelectColor.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :


import math
import config
import cv2


# print(len(config.colors))

# BGR转成RGB
picture = cv2.imread(config.picturePath, )
# picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
height, width, channel = picture.shape

for row in range(0, height):
    for col in range(0, width):

        # Get pixel
        pixel = picture[row, col, :]
        distance = 1000

        for colorIndex in range(0, len(config.colors)):

            # Get color
            color = config.colors[colorIndex]

            # 3通道
            if channel == 3:
                tempDistance = math.sqrt(math.pow(pixel[0] - color[0], 2) + math.pow(pixel[1] - color[1], 2) + math.pow(pixel[2] - color[2], 2))

            # 单通道
            elif channel == 1:
                tempDistance = math.fabs(pixel[0] - color[0])

            # 错误
            else:
                print("Channel is error!")

            # Change pixel color
            if tempDistance < distance:
                distance = tempDistance
                pixelColor = color

        # Set pixel color
        picture[row, col, :] = pixelColor

cv2.imwrite(config.StorePath + config.pixelPictureName, picture)