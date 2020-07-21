"""
描述：Numpy-创建数组
参考：https://www.runoob.com/numpy/numpy-array-creation.html
作者：王佳秋
日期：2020年7月20日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.empty()创建一个指定的形状(shape),数据类型(dtype)且未初始化的数组
    x = np.empty(shape=[3, 2], dtype=int)
    print("x.empty: ", x)

    # 2.numpy.zeros()创建指定大小的数组，数组元素以0来填充
    # 2.1默认为浮点数
    x = np.zeros(5)
    print("0数组：", x)
    # 2.2设置类型为整数
    y = np.zeros((5,), dtype=np.int)
    print('设置整数的数组：', y)
    # 2.3自定义类型
    z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
    print("自定义类型的数组：", z)

    # 3. numpy.ones()创建指定形状的数组，数组元素以1来填充。
    # 3.1默认为浮点数
    x = np.ones(5)
    print("ones默认浮点数的1数组：", x)
    # 3.2自定义类型
    x = np.ones([2, 2], dtype=int)
    print("自定义类型的1数组：", x)

    # 4.Numpy创建正态分布数组
    # 创建randn(size)服从X~N(0, 1)的正态分布随机数组
    a = np.random.randn(2, 3)
    print("创建randn(size)服从X~N(0, 1)的正态分布随机数组: ", a)

    # 5.Numpy创建随机分布整数数组
    """利用 randint([low,high],size) 创建一个整数型指定范围在 [low.high] 之间的数组："""
    a = np.random.randint(100, 200, (3, 3))
    print("a:", a)

    # 6.arange创建数组
    a = np.arange(10)
    b = np.arange(10, 20)
    c = np.arange(10, 20, 2)
    print("arange:", a)
    print(b)
    print(c)
