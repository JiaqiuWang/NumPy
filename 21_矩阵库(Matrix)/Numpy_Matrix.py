"""
描述：Numpy-矩阵库(Matrix)
参考：https://www.runoob.com/numpy/numpy-matrix.html
作者：王佳秋
日期：2020年7月27日
"""


import numpy as np
from numpy import matlib


if __name__ == "__main__":

    # 1.numpy.matlib.empty()返回一个新的矩阵
    print(np.matlib.empty((2, 2)))  # 填充为随机数据

    # 2.numpy.matlib.zeros()创建一个以 0 填充的矩阵
    print(np.matlib.zeros((2, 2)), "\n")

    # 3.numpy.matlib.ones()创建一个以 1 填充的矩阵
    print(np.matlib.ones((2, 2)), "\n")

    # 4.numpy.matlib.eye()返回一个矩阵，对角线元素为 1，其他位置为零
    print(np.matlib.eye(n=3, M=4, k=1, dtype=float), "\n")

    # 5.numpy.matlib.identity()返回给定大小的单位矩阵
    print(np.matlib.identity(5, dtype=float))  # 大小为 5，类型位浮点型

    # 6.numpy.matlib.rand()创建一个给定大小的矩阵，数据是随机填充的
    print(np.matlib.rand(3, 3), "\n")
    print("Type: ", type(np.matlib.rand(3, 3)))

    # 7.矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的
    i = np.matrix('1, 2; 3, 4')
    print(i)
    # 7.1 矩阵变成数组对象
    j = np.asarray(i)
    print(j)
    # 7.2 数组对象变成矩阵
    k = np.asmatrix(j)
    print(k)
