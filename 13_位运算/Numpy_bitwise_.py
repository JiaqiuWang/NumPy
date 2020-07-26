"""
描述：Numpy-位运算
参考：https://www.runoob.com/numpy/numpy-binary-operators.html
作者：王佳秋
日期：2020年7月25日
"""


import numpy as np


if __name__ == "__main__":

    # 1.bitwise_and()对数组中整数的二进制形式执行位与运算
    print("13与17的二进制形式：")
    a, b =13, 17
    print(bin(a), bin(b), "\n")
    print("13与17的位与：")
    print(np.bitwise_and(13, 17))

    # 2.bitwise_or()对数组中整数的二进制形式执行位或运算
    print("3与17的位或：")
    print(np.bitwise_or(13, 17))

    # 3.invert()对数组中的整数进行位取反运算，即0变成1,1变成0
    print("13的位反转，其中ndarray的dtype是uint8:")
    print(np.invert(np.array([13], dtype=np.uint8)), "\n")
    # 比较13和242的二进制表示，发现位的反转
    print("13的二进制表示：")
    print(np.binary_repr(13, width=8), "\n")
    print("242的二进制表示：")
    print(np.binary_repr(242, width=8), "\n")

    # 4.left_shift()将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的0
    print("将10左移两位：")
    print(np.left_shift(10, 2), "\n")
    print("10的二进制表示：")
    print(np.binary_repr(10, width=8), "\n")
    print("40的二进制表示：")
    print(np.binary_repr(40, width=8), "\n")

    # 5.right_shift()将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的0
    print("将40右移两位：")
    print(np.right_shift(40, 2), "\n")




