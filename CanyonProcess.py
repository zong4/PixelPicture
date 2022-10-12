# -*- coding : utf-8 -*-
# @Time      : 2022/6/4 10:50
# @Author    : Zong
# @File      : CanyonProcess.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :


import config
import cv2


picture = cv2.imread(config.picturePath, 0)
pictureProcessed = cv2.Sobel(picture, cv2.CV_64F, dx=1, dy=0)

cv2.imwrite("1.png", pictureProcessed)