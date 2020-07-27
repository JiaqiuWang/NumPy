"""
描述：Numpy-字节交换
参考：https://www.runoob.com/numpy/numpy-byte-swapping.html
作者：王佳秋
日期：2020年7月27日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.bytesswap()将 ndarray 中每个元素中的字节进行大小端转换
    a = np.array([1, 256, 8755], dtype=np.int16)
    print("我们的数组：\n", a, "\n")
    print('以十六进制表示内存中的数据：')
    print(map(hex, a))
    # byteswap() 函数通过传入 true 来原地交换
    print('调用 byteswap() 函数：')
    print(a.byteswap(True))
    print('十六进制形式：')
    print(map(hex, a))
    # 我们可以看到字节已经交换了




