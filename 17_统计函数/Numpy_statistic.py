"""
描述：Numpy-统计函数
参考：https://www.runoob.com/numpy/numpy-statistical-functions.html
作者：王佳秋
日期：2020年7月26日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.amin() 和 numpy.amax()用于计算数组中的元素沿指定轴的最大、最小值。
    a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
    print("我们的数组：\n", a, "\n")
    print("调用amin():\n", np.amin(a, 1), "\n")  # 沿轴1找到最小值
    print("再次调用amin():")
    print(np.amin(a, 0), "\n")
    print("调用amax():")
    print(np.amax(a), "\n")  # 如果不写轴参数，则默认找到数组中最大值
    print("再次调用amax():")
    print(np.amax(a, axis=0))

    # 2.numpy.ptp()计算数组中最大值与最小值的差（最大值 - 最小值）
    print("调用ptp():")
    print(np.ptp(a), "\n")
    print("沿轴1调用ptp():")
    print(np.ptp(a, axis=1), "\n")
    print("沿轴0调用ptp():")
    print(np.ptp(a, axis=0))

    # 3.numpy.percentile()百分位数
    a = np.array([[10, 7, 4], [3, 2, 1]])
    print("我们的数组：\n", a)
    print("调用percentile():")
    # 3.1 50% 的分位数，就是 a 里排序之后的中位数
    print(np.percentile(a, 50))
    # 3.2 axis为0
    print(np.percentile(a, 50, axis=0))
    # 3.3 axis为1
    print(np.percentile(a, 50, axis=1))
    # 3.4 保持维度不变
    print(np.percentile(a, 50, axis=1, keepdims=True))

    # 4.numpy.median()用于计算数组 a 中元素的中位数（中值）
    a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
    print("我们的数组：\n", a, "\n")
    print("调用median():")
    print(np.median(a), "\n")
    print("沿轴0调用median():\n", np.median(a, axis=0), "\n")
    print("沿轴1调用median():\n", np.median(a, axis=1), "\n")

    # 5.numpy.mean()返回数组中元素的算术平均值
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print("我们的数组：\n", a, "\n")
    print("调用mean():")
    print(np.mean(a), "\n")
    print('沿轴 0 调用 mean() 函数：')
    print(np.mean(a, axis=0), "\n")
    print('沿轴 1 调用 mean() 函数：')
    print(np.mean(a, axis=1))

    # 6.numpy.average()
    a = np.array([1, 2, 3, 4])
    print("我们的数组：\n", a, "\n")
    print('调用 average() 函数：')
    print(np.average(a), "\n")
    # 不指定权重时相当于 mean 函数
    wts = np.array([4, 3, 2, 1])
    print('再次调用 average() 函数：')
    print(np.average(a, weights=wts), "\n")
    # 如果 returned 参数设为 true，则返回权重的和
    print('权重的和：')
    print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))
    # 6.1 在多维数组中，可以指定用于计算的轴
    a = np.arange(6).reshape(3, 2)
    print("我们的数组：\n", a, "\n")
    print('修改后的数组：')
    wt = np.array([3, 5])
    print(np.average(a, axis=1, weights=wt), "\n")
    print('修改后的数组：')
    print(np.average(a, axis=1, weights=wt, returned=True))

    # 7.标准差
    print("数组标准差：", np.std([1, 2, 3, 4]))

    # 8.方差
    print(np.var([1, 2, 3, 4]))









