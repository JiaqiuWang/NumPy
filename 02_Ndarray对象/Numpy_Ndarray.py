"""
描述：Numpy-Ndarray对象
参考：https://www.runoob.com/numpy/numpy-ndarray-object.html
作者：王佳秋
日期：2020年7月19日
"""


import numpy as np


if __name__ == "__main__":

    # 1.基本形式
    a = np.array([1, 2, 3])
    print("a: ", a)

    # 2.多于一个维度
    b = np.array([[1, 2], [3, 4]])
    print("二个维度数组b:")
    print(b)

    # 3.最小维度
    c = np.array([1, 2, 3, 4, 5], ndmin=2)
    print("最小维度数组c: ")
    print(c)

    # 4.dtype参数
    d = np.array([1, 2, 3], dtype=complex)  # 参数类型是complex复数
    print("带有dtype参数的数组：", d)

