"""
描述：Numpy-从已有的数组创建数组
参考：https://www.runoob.com/numpy/numpy-array-from-existing-data.html
作者：王佳秋
日期：2020年7月21日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.asarray(x)将列表转换为ndarray
    x = [1, 2, 3]
    a = np.asarray(x)
    print(a)

    # 2.numpy.asarray(x)将元祖转换为ndarray
    x = (1, 2, 3)
    a = np.asarray(x)
    print(a)

    # 3.将元祖列表转换为ndarray
    x = [(1, 2, 3), (4, 5)]
    a = np.asarray(x)
    print(a)

    # 4.设置dtype参数
    x = [1, 2, 3]
    a = np.asarray(x, dtype=float)
    print(a)

    # 5.numpy.frombuffer()实现动态数组
    s = b'Hello World'  # 注意：buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。
    a = np.frombuffer(s, dtype='S1')
    print(a)
    # 5.1 实例2
    # s = 'Hello World'
    # a = np.frombuffer(s, dtype='S1')
    # print("非b:", a)  # 会报错：TypeError: a bytes-like object is required, not 'str'

    # 6.numpy.fromiter()方法从可迭代对象中建立ndarray对象，返回一维数组
    # 使用range函数创建列表对象
    list1 = range(5)
    print("list1: ", list1)
    it = iter(list1)
    print(it)
    # 使用迭代器创建ndarray
    x = np.fromiter(it, dtype=float)
    print("x:", x)

