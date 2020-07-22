"""
描述：Numpy-广播Broadcast
参考：https://www.runoob.com/numpy/numpy-broadcast.html
作者：王佳秋
日期：2020年7月22日
"""


import numpy as np


if __name__ == "__main__":

    # 1.如果两个数组a和b形状相同，a*b结果是对应元素相乘。
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    c = a * b
    print("c:\n", c)

    # 2.当运算中的2个数组形状不同时，numpy将自动触发广播机制。
    a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
    b = np.array([1, 2, 3])
    print("a,b维度不同，启动广播机制：a+b:\n", a + b)

    # 3.
    a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
    b = np.array([1, 2, 3])
    bb = np.tile(b, (4, 1))  # 重复b的各个维度 4 行 1列
    print("bb:\n", bb)
    print("a + bb:\n", a + bb)


