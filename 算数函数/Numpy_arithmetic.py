"""
描述：Numpy-算数函数 NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
需要注意的是数组必须具有相同的形状或符合数组广播规则。
参考：https://www.runoob.com/numpy/numpy-arithmetic-operations.html
作者：王佳秋
日期：2020年7月19日
"""


import numpy as np


def basic_methods():
    """基础的矩阵/数组加减乘除运算"""
    a = np.arange(9, dtype=np.float_).reshape(3, 3)
    print("第一个数组a: ")
    print(a)
    print('\n')
    print('第二个数组：')

    b = np.array([10, 10, 10])
    print(b)
    print('\n')

    print("两个数组相加：")
    print(np.add(a, b))
    print('\n')

    print("两个数组相减：")
    print(np.subtract(a, b))
    print('\n')

    print("两个数组相乘：")
    print(np.multiply(a, b))
    print('\n')

    print('两个数组相除：')
    print(np.divide(a, b))


def reciprocal():
    """numpy.reciprocal()函数返回参数逐元素的倒数。例如，1/4的倒数为4/1."""
    a = np.array([0.25, 1.33, 1, 100])
    print("我们的数组是：")
    print(a)
    print('\n')
    print("调用reciprocal函数：")
    print(np.reciprocal(a))


def power():
    """numpy.power()函数将第一个输入数组的元素作为底数，计算它与第二个输入数组中相应元素的幂"""
    a = np.array([10, 100, 1000])
    print("我们的数组是：")
    print(a)
    print('\n')
    print('调用power函数：')
    print(np.power(a, 2))
    print('\n')
    print('第二个数组：')
    b = np.array([1, 2, 3])
    print(b)
    print('\n')
    print('再次调用power函数：')
    print(np.power(a, b))


def mod_numpy():
    """numpy.mod()计算输入数组中相应元素的相除后的余数。函数numpy.remainder()也产生相同的结果。"""
    a = np.array([10, 20, 30])
    b = np.array([3, 5, 7])
    print('第一个数组：')
    print(a)
    print('\n')
    print("第二个数组：")
    print(b)
    print('\n')
    print("调用mod()函数：")
    print(np.mod(a, b))
    print('\n')
    print('调用remainder()函数：')
    print(np.remainder(a, b))


if __name__ == "__main__":

    # basic_methods()  # 基础的矩阵/数组加减乘除运算
    # reciprocal()  # 数组的逐元素倒数数组
    # power()  # 数组/矩阵的幂函数
    mod_numpy()  # 数组/矩阵的取余数
