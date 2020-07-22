"""
描述：Numpy-切片slice和索引index
参考：https://www.runoob.com/numpy/numpy-ndexing-and-slicing.html
作者：王佳秋
日期：2020年7月22日
"""


import numpy as np


if __name__ == "__main__":

    # 1.切片函数slice()
    a = np.arange(10)
    print("a:", a)
    s = slice(2, 7, 2)  # 从索引2开始到索引7停止，间隔为2
    print("切片：", a[s])
    # 冒号: 使用
    a = np.arange(10)
    b = a[5]
    print("冒号的使用:", b)
    print("冒号的使用：", a[2:])
    print("冒号的使用：", a[2:5])

    # 2.多维数组同样适用于索引提取方法
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print("多维数组：", a)
    print("多维数组的切片a[1:] ", a[1:])

    # 3.切片还可以包括省略号...，来使选择元组的长度与数组的维度相同，
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print("第2列元素：", a[..., 1])
    print("第2行元素：", a[1, ...])
    print("第2列及剩下的所有元素：", a[..., 1:])

    # 4.在多维数组切片中，使用,区分维数
    a = np.arange(0, 12)
    print("a:", a)
    a = a.reshape(3, 4)
    print("reshape-a:", a)
    print(a[0:2, 1:3])

    # 5.在多维数组中，非连续索引切片
    a = np.arange(0, 6)
    print("a:", a)
    b = np.arange(0, 25)
    print("b:", b)
    b.shape = (5, 5)
    print("reshape-b:")
    print(b)
    # 切片向量既可以为array，也可以为List类型
    r = np.array([0, 1, 4])  # r = [0, 1, 4]
    c = [1, 2, 4]  # c = np.array([1, 2, 4])
    print("a:\n", a)
    print("a_slice:\n", a[r])
    print("b:\n", b)
    print("b_slice:\n", b[r, :][:, c])

    a = np.arange(0, 80)
    a.shape = (8, 10)
    print("reshape-a:\n", a)
    """a[1:3, 2:5] 中逗号左边的为行，
    右边为列（第 2 行到第 3 行，第 3 列到第 5 列）"""
    print("在多维数组中的非连续索引切片:\n", a[1:3, 2:5])


