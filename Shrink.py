# -*- coding : utf-8 -*-
# @Time      : 2022/6/3 15:08
# @Author    : Zong
# @File      : main.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :


import math
import numpy as np
import config
import cv2


picture = cv2.imread(config.picturePath)

height, width, channel = picture.shape
# print(picture.shape)

# isAddBlackEdge = False, 向下取整
pixelBlockHeight = math.floor(height / config.pixelPictureHeight)
pixelBlockWidth = math.floor(width / config.pixelPictureWidth)

# Start point
startRow = config.startRow
startCol = config.startCol

# One block reflect one pixel
block = np.empty([pixelBlockHeight, pixelBlockWidth, channel], dtype='uint8')
# print(block.shape)

# Every block
for blockNumRow in range(0, config.pixelPictureWidth):
    for blockNumCol in range(0, config.pixelPictureHeight):

        # Assign numbers
        block = picture[startRow : startRow + pixelBlockHeight, startCol : startCol + pixelBlockWidth, :]
        # print(block.shape)

        # Every channel
        for page in range(0, channel):
            mean = np.mean(block[:, :, page])
            std = np.std(block[:, :, page])

            # 剔除2σ异常值
            numMaxEdge = mean + 1 * std
            numMinEdge = mean - 1 * std
            usefulNum = []

            for blockRow in range(0, pixelBlockHeight):
                for blockCol in range(0, pixelBlockWidth):

                    # 如果在范围内，加入有效值数组内
                    if (block[blockRow, blockCol, page] <= numMaxEdge) and (block[blockRow, blockCol, page] >= numMinEdge):
                        usefulNum.append(block[blockRow, blockCol, page])

            # 如果开启平滑
            if config.isUseAverage:
                # print(len(usefulNum))
                config.pixelPicture[blockNumRow, blockNumCol, page] = np.mean(usefulNum)
            else:
                config.pixelPicture[blockNumRow, blockNumCol, page] = max(usefulNum, key=usefulNum.count)

        # Next block row
        startCol = startCol + pixelBlockWidth

    startRow = startRow + pixelBlockHeight
    startCol = config.startCol

cv2.imwrite(config.StorePath + config.pixelPictureName, config.pixelPicture)