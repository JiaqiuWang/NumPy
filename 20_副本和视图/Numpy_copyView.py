"""
描述：Numpy-副本和视图
参考：https://www.runoob.com/numpy/numpy-copies-and-views.html
作者：王佳秋
日期：2020年7月27日
"""


import numpy as np


if __name__ == "__main__":

    """一.无复制"""
    a = np.arange(6)
    print("我们的数组：\n", a)
    print('调用 id() 函数：')
    print(id(a))
    print('a 赋值给 b：')
    b = a
    print("b:\n", b)
    print('b 拥有与a相同的 id()：')
    print(id(b))
    print('修改 b 的形状：')
    b.shape = (3, 2)
    print(b)
    print('a 的形状也修改了：')
    print(a)

    """二.视图或潜拷贝"""
    # 2.1 numpy.view()创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数
    # 最开始 a 是个 3X2 的数组
    a = np.arange(6).reshape(3, 2)
    print("我们的数组：\n", a)
    print('创建 a 的视图：')
    b = a.view()
    print("b:\n", b)
    print('两个数组的 id() 不同：')
    print('a 的 id()：', id(a))
    print('b 的 id()：', id(b))
    # 修改 b 的形状，并不会修改 a
    b.shape = (2, 3)
    print('b修改后的形状：\n', b)
    print('a的形状：\n', a)

    # 2.2 使用切片创建视图修改数据会影响到原始数组
    arr = np.arange(12)
    print("我们的数组：\n", arr)
    print('创建切片：')
    a = arr[3:]
    print(a)
    b = arr[3:]
    a[1] = 123
    b[2] = 234
    print("切片修改后的数组：\n", arr)
    print(id(a), id(b), id(arr[3:]))

    """三.副本或深拷贝"""
    a = np.array([[10, 10], [2, 3], [4, 5]])
    print("我们的数组：\n", a)
    print('创建 a 的深层副本：')
    b = a.copy()
    print('数组 b：')
    print("b:", b)
    # b 与 a 不共享任何内容
    print('我们能通过写入 b 来写入 a 吗？')
    print("b is a?", b is a)
    print('修改 b 的内容：')
    b[0, 0] = 100
    print('修改后的数组 b：')
    print(b)
    print('a 保持不变：')
    print(a)
