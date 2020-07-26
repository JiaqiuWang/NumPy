"""
描述：Numpy-迭代数组
参考：https://www.runoob.com/numpy/numpy-terating-over-array.html
作者：王佳秋
日期：2020年7月23日
"""


import numpy as np


if __name__ == "__main__":

    # 1.对数组进行迭代
    a = np.arange(6).reshape(2, 3)
    print("a:\n", a)
    print("迭代地输出元素：\n")
    for x in np.nditer(a):
        print("x:", x, end=", ")
    print("\n")

    #  2.
    a = np.arange(6).reshape(2, 3)
    print("a.T:\n", a.T)
    for x in np.nditer(a.T):
        print("x:", x, end=", ")
    print("\n")
    """从上述例子可以看出，a 和 a.T 的遍历顺序是一样的，
    也就是他们在内存中的存储顺序也是一样的，但是 a.T.copy(order = 'C') 的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。"""
    for x in np.nditer(a.T.copy(order='C')):
        print("x:", x, end=", ")
    print("\n")

    # 3.控制便利顺序
    a = np.arange(0, 60, 5)
    a = a.reshape(3, -1)
    print("原始数组：\n", a)
    print("原始数组的转置：\n", a.T)

    print("行优先排序：\n", )
    c = a.T.copy(order='C')
    for x in np.nditer(c):
        print("x:", x, end=", ")
    print("\n")

    print("列优先排序：\n")
    c = a.T.copy(order='F')
    for x in np.nditer(c):
        print("x:", x, end=", ")

    # 4.修改数组中元素的值
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print("原始数组：\n")
    print(a)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2 * x
    print("修改后的数组：\n", a)

    # 5.迭代器遍历对应于每列，并组合为一维数组
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print("原始数组：\n", a)
    print("修改后的数组：\n")
    # external_loop:给出的值是具有多个值的一维数组，而不是零维数组
    for x in np.nditer(a, flags=['external_loop'], order='F'):  # F列优先
        print("x:", x, end=", ")
    print()

    # 6.广播迭代:数组 b 被广播到 a 的大小
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print("第一个数组：\n", a)
    b = np.array([1, 2, 3, 4], dtype=int)
    print("第二个数组：\n", b)
    print("修改后的数组：")
    for x, y in np.nditer([a, b]):
        print("%d:%d" % (x, y), end=", ")
    print()









