"""
描述：Numpy-数组属性
参考：https://www.runoob.com/numpy/numpy-array-attributes.html
作者：王佳秋
日期：2020年7月19日
"""


import numpy as np


if __name__ == "__main__":

    # 1.1ndarray.ndim秩，即轴的数量或维度的数量
    a = np.arange(24)
    print(a)
    print("a的秩：", a.ndim)
    # 1.2现在调整其大小
    b = a.reshape(2, 4, -1)  # b现在拥有三个维度, reshape()函数中的参数需要满足乘积等于数组中数据总数.
    print("b的维度", b)
    print("b的维度", b.ndim)

    # 2.1 ndarray.shape表示数组的维度，返回一个数组。
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("shape返回数组的维度：", a.shape)
    # 2.2调整数组大小。
    a = a.reshape(3, -1)
    print("调整数组大小：", a)

    # 3.1 ndarray.itemsize以字节的形式返回数组中每一个元素的大小
    # 数组的dtype为int8(一个字节)
    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    print("itemsize: ", x.itemsize)

    # 3.2 数组的dtype现在为float64(八个字节)
    y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print(y.itemsize)

    # 4.1 ndarray.flags
    x = np.array([1, 2, 3, 4, 5])
    print("x.flags: ", x.flags)

