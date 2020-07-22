"""
描述：Numpy-从数值范围arange创建数组
参考：https://www.runoob.com/numpy/numpy-array-from-numerical-ranges.html
作者：王佳秋
日期：2020年7月21日
"""


import numpy as np


if __name__ == "__main__":

    # 1.生成0到5的数组
    x = np.arange(5)
    print(x)

    # 2.设置返回类型为float
    x = np.arange(5, dtype=float)
    print("x:", x)

    # 3.设置起始值、终止值步长
    x = np.arange(10, 20, 2)
    print(x)

    # 4.numpy.linspace()函数用于创建一个由等差数列构成的一维数组
    # 4.1 设置起始点为1，终止点为10，数列个数为10
    a = np.linspace(start=1, stop=10, num=10)
    print("等差数列：", a)
    # 4.2 设置元素全部是1的等差数列
    a = np.linspace(1, 1, 10)
    print("元素全部是1的等差数列: ", a)
    # 4.3 将endpoint设置为false，不包含终止值
    a = np.linspace(10, 20, 5, endpoint=False)
    print("将endpoint设置为false，不包含终止值:", a)
    # 4.4 将endpoint设置为true，则会包含20，以下实例设置间距
    a = np.linspace(1, 10, 10, retstep=True)
    print("显示数列的间距：", a)
    # 4.5 拓展例子
    b = np.linspace(1, 10, 10).reshape(10, 1)
    print("b:", b)

    # 5.numpy.logsapce()函数用于创建一个等比数列
    # 5.1 默认底数是10
    a = np.logspace(1.0, 2.0, num=10)
    print("等比数列logsapce(): ", a)
    # 5.2 将对数的底数设置为2
    a = np.logspace(start=0, stop=9, num=10, base=2)
    print("将对数的底数设置为2的等比数列：", a)
    
    