"""
描述：Numpy-排序、条件刷选函数
参考：https://www.runoob.com/numpy/numpy-sort-search.html
作者：王佳秋
日期：2020年7月26日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.sort()返回输入数组的排序副本
    a = np.array([[3, 7], [9, 1]])
    print("我们的数组：\n", a, "\n")
    print("调用 sort() 函数：")
    print(np.sort(a), "\n")
    print('按列排序：')
    print(np.sort(a, axis=0), "\n")
    # 在 sort 函数中排序字段
    dt = np.dtype([('name', 'S10'), ('age', int)])
    a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
    print("我们的数组：\n", a, "\n")
    print("按name排序：")
    print(np.sort(a, order='name'))

    # 2.numpy.argsort()返回的是数组值从小到大的索引值
    x = np.array([3, 1, 2])
    print("我们的数组：\n", a, "\n")
    print('对 x 调用 argsort() 函数：')
    y = np.argsort(x)
    print(y, "\n")
    print('以排序后的顺序重构原数组：')
    print(x[y], "\n")
    print('使用循环重构原数组：')
    for i in y:
        print(x[i], end=" ")

    # 3.numpy.lexsort()对多个序列进行排序
    nm = ('raju', 'anil', 'ravi', 'amar')
    dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
    ind = np.lexsort((dv, nm))
    print("(dv, nm):", (dv, nm))
    print('调用 lexsort() 函数：')
    print("索引ind:", ind)
    print('使用这个索引来获取排序后的数据：')
    print([nm[i] + ", " + dv[i] for i in ind])

    # 3.1 lexsort()实现多列成绩排序问题
    # 录入了四位同学的成绩，按照总分排序，总分相同时语文高的优先
    math = (10, 20, 50, 10)
    chinese = (30, 50, 40, 60)
    total = (40, 70, 90, 70)
    # 将优先级高的项放在后面
    ind = np.lexsort((math, chinese, total))  # 只返回顺序索引
    print("ind-scores: ", ind)
    for i in ind:
        print(total[i], chinese[i], math[i])
    # 注释：输出，是按总成绩排序，相同时语文成绩优先级更高:

    # 4.numpy.sort_complex()复数排序
    print("复数数组的排序：", np.sort_complex([5, 3, 6, 2, 1]))
    print("复数数组的排序：", np.sort_complex([1+2j, 2-1j, 3-2j, 3-3j, 3+5j]))

    # 5.numpy.partition()指定一个数，对数组进行分区
    a = np.array([3, 4, 2, 1])
    print("partition()数组分区：", np.partition(a, 3))
    print(np.partition(a, (1, 3)))  # 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间

    # 6.numpy.argpartition()可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
    arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
    print("argpartition()", arr[np.argpartition(arr, 2)[2]])
    print("argpartition()", arr[np.argpartition(arr, -2)[-2]])

    # 7.numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引
    a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
    print("我们的数组：\n", a, "\n")
    print('调用 argmax() 函数：')
    print(np.argmax(a), "\n")
    print('展开数组：', a.flatten(), "\n")
    print('沿轴 0 的最大值索引：')
    maxindex = np.argmax(a, axis=0)
    print("maxindex:", maxindex, "\n")
    print('沿轴 1 的最大值索引：')
    maxindex = np.argmax(a, axis=1)
    print(maxindex, "\n")
    print('调用 argmin() 函数：')
    minindex = np.argmin(a)
    print("min_index:", minindex, "\n")
    print('展开数组中的最小值：')
    print(a.flatten()[minindex], "\n")
    print('沿轴 0 的最小值索引：')
    minindex = np.argmin(a, axis=0)
    print(minindex, "\n")
    print("沿轴1的最小值索引：")
    minindex = np.argmin(a, axis=1)
    print(minindex)

    # 8.numpy.nonzero()返回输入数组中非零元素的索引
    a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
    print("我们的数组：\n", a, "\n")
    print('调用 nonzero() 函数：')
    print(np.nonzero(a))  # 竖着看输出两个的两行一维数组，即(0,0), (0,1)
    print('使用这些索引来获取满足条件的元素：')
    print(a[np.nonzero(a)])

    # 9.numpy.where()返回输入数组中满足给定条件的元素的索引
    x = np.arange(9.).reshape(3, 3)
    print("我们的数组：\n", x, "\n")
    print('大于 3 的元素的索引：')
    y = np.where(x > 3)
    print(y)
    print('使用这些索引来获取满足条件的元素：')
    print(x[y])

    # 10.numpy.extract()根据某个条件从数组中抽取元素，返回满条件的元素
    # 定义条件, 选择偶数元素
    condition = np.mod(x, 2) == 0
    print('按元素的条件值：')
    print(condition)
    print('使用条件提取元素：')
    print(np.extract(condition, x))







