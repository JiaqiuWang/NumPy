"""
描述：Numpy-数组操作
参考：https://www.runoob.com/numpy/numpy-array-manipulation.html
作者：王佳秋
日期：2020年7月23日
目录：一.修改数组形状
      二.翻转数组
      三.修改数组维度
      四.连接数组
      五.分割数组
      六.数组元素的添加与删除
"""


import numpy as np


if __name__ == "__main__":

    """一.修改数据形状"""
    # 1.1.numpy.reshape:在不改变数据的条件下修改形状
    a = np.arange(8)
    print("原始数据：\n", a)
    b = a.reshape(4, 2)
    print("\n修改后的数组：\n", b)

    # 1.2.numpy.ndarray.flat:数组元素迭代器
    a = np.arange(9).reshape(3, 3)
    print("原始数组：")
    for row in a:
        print(row)
    # 对数组中每个元素都进行处理，可使用flat属性，该属性是一个数组元素迭代器
    print("迭代后的数组：")
    for element in a.flat:
        print(element)

    # 1.3.numpy.ndarray.flatten返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
    a = np.arange(8).reshape(2, 4)
    print("原始数组：\n", a)
    # 默认按行
    print("展开的数组：", a.flatten(), "\n")
    print("按列顺序展开数组：", a.flatten(order='F'))

    # 1.4.numpy.ravel()展平的数组元素
    a = np.arange(8).reshape(2, 4)
    print("原始数组：\n", a, "\n")
    print("默认以行优先C顺序调用ravel()函数之后：", a.ravel(), "\n")
    print("按照列优先F顺序调用ravel函数之后：", a.ravel(order='F'))

    """二.翻转数组"""
    # 2.1 numpy.tranpose()函数用于对换数组的维度
    a = np.arange(12).reshape(3, 4)
    print("原始数组：\n", a, "\n")
    print("对换数组：\n", np.transpose(a), "\n")
    # 2.1.1 numpy.ndarray.T 类似numpy.transpose
    print("转置数组a.T：\n", a.T)

    # 2.2 numpy.rollaxis()函数向后滚动特定的轴到一个特定位置
    # 创建了三维数组ndarray
    a = np.arange(8).reshape((2, 2, 2))
    print("三维数组：\n", a, "\n")
    # 将轴2滚动到轴0（宽度到深度）
    print("调用rollaxis函数()：\n", np.rollaxis(a, 2))
    # 将轴0滚动到轴1：（宽度到高度）
    print("\n调用rollaxis()函数：\n", np.rollaxis(a, 2, 1))

    # 2.3 numpy.swapaxes()函数用于交换数组的两个轴
    # 创建了三维数组ndarray
    a = np.arange(8).reshape((2, 2, 2))
    print("三维数组：\n", a, "\n")
    # 现在交换轴0（深度方向）到轴2（宽度方向）
    print("调用swapaxes()函数后的数组：\n", np.swapaxes(a, 2, 0))

    """三.修改数组维度"""
    # 3.1 numpy.broadcast()产生模仿广播的对象
    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])
    # 对y广播x
    b = np.broadcast(x, y)
    # 它拥有iterator属性，基于自身组件的迭代器元祖
    print("对y广播x:")
    r, c = b.iters
    print(next(r), next(c))
    print(next(r), next(c), "\n")
    # shape属性返回广播对象的形状
    print("广播对象的形状：")
    b = np.broadcast(x, y)
    c = np.empty(b.shape)
    print("手动使用broadcast将x与y相加：")
    print(c.shape, "\n")
    c.flat = [u + v for (u, v) in b]
    print("调用flat函数：", c, "\n")
    # 获得了和NumPy内建的广播支持相同的结果
    print('x与y的和：\n', x + y)

    # 3.2 numpy.broadcast_to() 函数将数组广播到新形状。
    a = np.arange(4).reshape(1, 4)
    print("原数组：\n", a, "\n")
    print("调用broadcast_to函数后：\n", np.broadcast_to(a, (4, 4)))

    # 3.3 numpy.expand_dims()通过在指定位置插入新的轴来扩展数组形状
    x = np.array([[1, 2], [3, 4]])
    print("数组x:\n", x, "\n")
    y = np.expand_dims(x, axis=0)
    print("数组y：\n", y, "\n")
    print("数组x和y的形状：\n")
    print(x.shape, y.shape, "\n")
    # 在位置1插入轴
    y = np.expand_dims(x, axis=1)
    print("在位置1插入轴之后的数组y:\n", y, "\n")
    print("x.ndim和y。ndim: \n", x.ndim, y.ndim, "\n")
    print("x.shape和y.shape:", x.shape, y.shape)

    # 3.4 numpy.squeeze()函数从给定数组的形状中删除一维的条目。
    x = np.arange(9).reshape((1, 3, 3))
    print("x:\n", x, "\n")
    y = np.squeeze(x)
    print("y:\n", y)
    print("数组x和y的形状：", x.shape, y.shape)

    """四.连接数组"""
    # 4.1 numpy.concatenate()函数用于沿指定轴连接相同形状的两个或多个数组。
    a = np.array([[1, 2], [3, 4]])
    print("第一个数组：\n", a, "\n")
    b = np.array([[5, 6], [7, 8]])
    print("第二个数组：\n", b)
    # 两个数组的维度相同
    print("沿轴0连接两个数组：\n", np.concatenate((a, b), axis=0), "\n")
    print("沿轴1连接两个数组：\n", np.concatenate((a, b), axis=1))

    # 4.2 numpy.stack()函数用于沿新轴连接数组序列
    a = np.array([[1, 2], [3, 4]])
    print("第一个数组：\n", a, "\n")
    b = np.array([[5, 6], [7, 8]])
    print("第二个数组：\n", b, "\n")
    print("沿轴0堆叠两个数组：\n", np.stack(arrays=(a, b), axis=0), "\n")
    print("沿轴1堆叠两个数组：\n", np.stack(arrays=(a, b), axis=1), "\n")

    # 4.3 numpy.hstack()函数通过水平堆叠来生成数组
    a = np.array([[1, 2], [3, 4]])
    print("第一个数组：\n", a, "\n")
    b = np.array([[5, 6], [7, 8]])
    print("第二个数组：\n", b, "\n")
    print("水平堆叠：\n", np.hstack((a, b)), "\n")

    # 4.4 numpy.vstack()函数通过垂直来生成数组
    a = np.array([[1, 2], [3, 4]])
    print("第一个数组：\n", a, "\n")
    b = np.array([[5, 6], [7, 8]])
    print("第二个数组：\n", b, "\n")
    print("竖直堆叠：\n", np.vstack((a, b)), "\n")

    """五.分割数组"""
    # 5.1 numpy.split()函数沿特定的轴将数组分割为子数组
    a = np.arange(9)
    print("第一个数组：\n", a, "\n")
    print("将数组分为3个大小相等的子数组：\n", np.split(ary=a, indices_or_sections=3, axis=0), "\n")
    print("将数组在一维数组中标明的位置分割：\n", np.split(ary=a, indices_or_sections=[4, 7], axis=0), "\n")

    # 5.2 numpy.hsplit()函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组
    # numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整
    harr = np.floor(10 * np.random.random((2, 6)))  # random.random()返回[0, 1)区间的浮点数
    # print("hsplit: \n", np.floor(10 * np.random.random((2, 6))))
    print("原harr:\n", harr, "\n")
    print("拆分后：", np.hsplit(harr, 2))
    print("拆分后：", np.hsplit(harr, 3))

    """六.数组元素的添加与删除"""
    # 6.1 numpy.resize()返回指定大小的新数组
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("第一个数组：\n", a, "\n")
    print("第一个数组的形状：\n", a.shape, "\n")
    b = np.resize(a, (3, 2))
    print("第二个数组：\n", b, "\n")
    print("第二个数组的形状：\n", b.shape, "\n")
    # 修改第二个数组的大小，a的第一行在b中重复出现，因为尺寸变大了
    print("修改第二个数组的大小：\n", np.resize(a, (3, 3)))

    # 6.1 numpy.append()在数组的末尾添加值
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("第一个数组：\n", a, "\n")
    print("想数组添加元素：\n", np.append(a, [7, 8, 9, 10]), "\n")
    print("沿轴0添加元素：\n", np.append(a, [[7, 8, 9]], axis=0))
    print("沿轴1添加元素：\n", np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

    # 6.2 numpy.insert()在给定索引之前，沿给定轴在输入数组中插入值
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print("第一个数组：\n", a, "\n")
    print("未传递axis参数，在插入之前输入数据会被展开：\n", np.insert(a, 3, [11, 12]), "\n")
    print("传递了axis参数，会广播值数组来配输入数组。")
    print("沿轴0广播：\n", np.insert(a, 1, [11], axis=0), "\n")
    print("沿轴1广播：\n", np.insert(a, 1, 11, axis=1), "\n")

    # 6.3 numpy.delete()删掉某个轴的子数组，并返回删除后的新数组
    a = np.arange(12).reshape(3, 4)
    print("第一个数组：\n", a, "\n")
    print("未传递axis参数，在插入之前输入数据会被展开：\n", np.delete(a, 5), "\n")
    print("删除第二列：\n", np.delete(a, 1, axis=1), "\n")
    print("包含从数组中删除的替代值的切片：")
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(a[::2])
    print(np.s_[::2])
    s = slice(0, len(a), 2)  # 从索引 2 开始到索引 7 停止，间隔为2
    print(np.delete(a, s))

    # 6.3 numpy.unique()用于去除数组中的重复元素
    a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
    print("第一个数组：\n", a, "\n")
    print("第一个数组的去重值：\n", np.unique(a), "\n")
    print("保留的-去重数组的索引数组：")
    u, indices = np.unique(a, return_index=True)
    print("indices:", indices, "\n")
    print("去掉的-去重数组的下标：")
    u, indices = np.unique(a, return_inverse=True)
    print("u:", u)
    print("indices:", indices)
    print("使用下标重构原数组：", u[indices], "\n")
    print("保留的-返回去重元素的重复数量")
    u, indices = np.unique(a, return_counts=True)
    print("u:", u)
    print("indices:", indices)

