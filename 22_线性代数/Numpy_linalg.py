"""
描述：Numpy-线性代数
参考：https://www.runoob.com/numpy/numpy-linear-algebra.html
作者：王佳秋
日期：2020年7月27日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.dot()两个数组的点积，即元素对应相乘。
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[11, 12], [13, 14]])
    print("dot:", np.dot(a, b))  # 矩阵乘积
    """计算式：[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]"""

    # 2.numpy.vdot()两个向量的点积
    print("vdot将数组展开计算内积-对应元素相乘再相加：")
    print(np.vdot(a, b))
    """计算式：1*11 + 2*12 + 3*13 + 4*14 = 130"""

    # 3.numpy.inner()返回两个数组的内积；对于更高的维度，它返回最后一个轴上的和的乘积
    # 3.1 一维数组间的内积
    print("数组内积：", np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))
    # 3.2 多维数组的内积
    a = np.array([[1, 2], [3, 4]])
    print("数组a: \n", a)
    b = np.array([[11, 12], [13, 14]])
    print("数组b: \n", b)
    print("a与b的数组内积：\n", np.inner(a, b))

    # 4.numpy.matmul()返回两个数组的矩阵乘积
    # 4.1 对于二维数组，它就是矩阵乘法
    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    print("矩阵乘法：\n", np.matmul(a, b))
    # 4.2 二维和一维运算
    a = [[1, 0], [0, 1]]
    b = [1, 2]
    print(np.matmul(a, b))
    print(np.matmul(b, a))
    # 4.3 维度大于二的数组
    a = np.arange(8).reshape((2, 2, 2))
    b = np.arange(4).reshape(2, 2)
    print(a)
    print(b)
    print(np.matmul(a, b))

    # 5.numpy.linalg.det()计算输入矩阵的行列式
    # 5.1 2 * 2的方阵
    a = np.array([[1, 2], [3, 4]])
    print("方阵的行列式：", np.linalg.det(a))
    # 5.2 3 * 3的方阵
    b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print("3 * 3方阵：\n", b)
    print("其行列式：", np.linalg.det(b))
    # 复习行列式的定义
    print(6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2))

    # 6.numpy.linalg.solve()给出了矩阵形式的线性方程的解
    # numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
    x = np.array([[1, 2], [3, 4]])
    y = np.linalg.inv(x)
    print("原始矩阵x：\n", x)
    print("x的逆矩阵y：\n", y)
    print("x与其逆矩阵y点积：\n", np.dot(x, y))
    # 6.1 现在创建一个矩阵A的逆矩阵:
    a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
    print('数组 a：\n', a)
    ainv = np.linalg.inv(a)
    print('a的逆矩阵：\n', ainv)
    print('矩阵 b：')
    b = np.array([[6], [-4], [27]])
    print(b)
    print("计算：A^(-1)B:")
    x = np.linalg.solve(a, b)
    print(x)
    # 这就是线性方向 x = 5, y = 3, z = -2 的解
    """结果也可以使用以下函数获取："""
    x = np.dot(ainv, b)
    print("计算：A^(-1)B:\n", x)











