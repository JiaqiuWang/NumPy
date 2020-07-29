"""
描述：Numpy-IO
参考：https://www.runoob.com/numpy/numpy-io.html
作者：王佳秋
日期：2020年7月29日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中
    a = np.array([1, 2, 3, 4, 5])
    # 1.1 保存到 outfile.npy文件上
    np.save('outfile.npy', a)
    # 1.2 # 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
    np.save('outfile2', a)

    #  2.numpy.load() 函数来读取数据就可以正常显示了
    b = np.load('outfile.npy')
    print("load outfile.npy:", b, "\n")

    # 3.numpy.savez()将多个数组保存到以 npz 为扩展名的文件中
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.arange(0, 1.0, 0.1)
    c = np.sin(b)
    print(a, b, c)
    # c 使用了关键字参数 sin_array
    np.savez("runoob.npz", a, b, sin_array=c)
    r = np.load("runoob.npz")
    print("查看各个数组名称：", r.files)
    print("数组a:", r["arr_0"])
    print("数组b:", r["arr_1"])
    print("数组c:", r["sin_array"])

    # 4.numpy.savetxt()以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据
    # 4.1 普通的
    a = np.array([1, 2, 3, 4, 5])
    np.savetxt('out.txt', a)
    b = np.loadtxt('out.txt')
    print(b)
    # 4.2 使用delimiter参数
    a = np.arange(0, 10, 0.5).reshape(4, -1)
    print("原始数组a：\n", a)
    np.savetxt("out.txt", a, fmt="%d", delimiter=",")  # 改为保存整数，以逗号分隔
    b = np.loadtxt("out.txt", delimiter=",")  # load 时要指定为逗号分隔
    print("b:", b)















