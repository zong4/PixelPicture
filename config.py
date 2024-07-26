# -*- coding : utf-8 -*-
# @Time      : 2022/6/3 15:17
# @Author    : Zong
# @File      : config.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :


import numpy as np


# Global
picturePath = r"your picture path"
StorePath = picturePath
pixelPictureName = "your picture name"

# Target
pixelPictureHeight = 64
pixelPictureWidth = 64
pixelPictureChannel = 3 # or 1

# Array
pixelPicture = np.empty([pixelPictureHeight, pixelPictureWidth, pixelPictureChannel], dtype='uint8')


# Shrink
# Black is (0, 0, 0), 如果像素不够，是否要在外部添加黑框
isAddBlackEdge = False

# 是否使用颜色平滑，默认不使用（不会改变颜色）
isUseAverage = False

# Start point
startRow = 0
startCol = 0


# Kmeans
# Keams聚类个数
keamsNum = 8


# SelectColor
colors = []

singleColor = [1, 1, 1]
colors.append(singleColor)
singleColor = [69, 201, 213]
colors.append(singleColor)
singleColor = [62, 88, 163]
colors.append(singleColor)
singleColor = [22, 35, 80]
colors.append(singleColor)
singleColor = [250, 226, 214]
colors.append(singleColor)
singleColor = [94, 88, 88]
colors.append(singleColor)
singleColor = [205, 206, 208]
colors.append(singleColor)
singleColor = [226, 188, 177]
colors.append(singleColor)

# Opencv默认BGR
for colorIndex in range(0, len(colors)):
    color = colors[colorIndex]

    R = color[0]
    color[0] = color[2]
    color[2] = R

print("Color is OK!")

