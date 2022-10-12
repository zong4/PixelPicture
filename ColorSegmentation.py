# -*- coding : utf-8 -*-
# @Time      : 2022/6/3 16:32
# @Author    : Zong
# @File      : ColorSegmentation.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :


import numpy as np
import config
import cv2
from sklearn.cluster import KMeans


# 转换数据维度
picture = cv2.imread(config.picturePath)
pictureFlatten = picture.reshape((picture.shape[0] * picture.shape[1], picture.shape[2]))


# 聚类
# 构造聚类器（基本都缺省）
# estimator = KMeans(config.keamsNum, init='k-means++')

# 自定义初始点
estimator = KMeans(len(config.colors), init=config.colors, n_init=1, max_iter=10000)

estimator.fit(pictureFlatten)

# 获取聚类中心
centroids = estimator.cluster_centers_

print(centroids)

# 可视化
# 使用算法跑出中心点，生成一个矩阵，为数据可视化做准备
result = []
result_width = 200
result_height_per_center = 80
# 获取图片色彩层数
n_channels = pictureFlatten.shape[1]

for center_index in range(0, len(config.colors)):
    result.append(np.full((result_width * result_height_per_center, n_channels), centroids[center_index], dtype=int))

result = np.array(result)
result = result.reshape((result_height_per_center * len(config.colors), result_width, n_channels))
result=result.astype(np.uint8)
cv2.imwrite("colorCard.png", result)