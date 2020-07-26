"""
描述：Numpy-数学函数
参考：https://www.runoob.com/numpy/numpy-mathematical-functions.html
作者：王佳秋
日期：2020年7月26日
"""


import numpy as np


if __name__ == "__main__":

    # 1.三角函数：sin(), cos(), tan()
    a = np.array([0, 30, 45, 60, 90])
    print("不同角度的正弦值：")
    # 通过乘 pi / 180 转化为弧度
    print(np.sin(a * np.pi/180), "\n")
    print("数组中角度的余弦值：")
    print(np.cos(a * np.pi/180), "\n")
    print("数组中角度的正切值：")
    print(np.tan(a * np.pi / 180))

    # 2.反三角函数arcsin(), arccos(), arctan()
    print("含有正弦值的数组：")
    sin = np.sin(a*np.pi/180)
    print(sin, "\n")
    print("计算角度的反正弦，返回值以弧度为单位：")
    inv = np.arcsin(sin)
    print(inv, "\n")
    print('arccos和arctan函数行为类似：')
    cos = np.cos(a*np.pi/180)
    print(cos, "\n")
    print("反余弦：")
    inv = np.arccos(cos)
    print(inv, "\n")
    print("角度制单位：")
    print(np.degrees(inv), "\n")
    print('tan函数：')
    tan = np.tan(a*np.pi/180)
    print(tan, "\n")
    print('反正切：')
    inv = np.arctan(tan)
    print(inv, "\n")
    print("角度制单位：")
    print(np.degrees((inv)))

    # 3. 舍入函数 numpy.around()返回指定数字的四舍五入值
    a = np.array([1.0, 5.55, 123, 0.567, 25.532])
    print("原数组：", a, "\n")
    print("舍入后：\n", np.around(a))
    print("舍入后：\n", np.around(a, decimals=1))
    print("舍入后：\n", np.around(a, decimals=-1))  # 若值为-n，则对小数点左边第n位近似；

    # 4. numpy.floor()返回小于或等于指定表达式的最大整数，即向下取整
    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print("提供的数组：\n", a, "\n")
    print("修改后的数组：", np.floor(a))

    # 5.numpy.ceil()返回大于或等于指定表达式的最小整数，即向上取整
    print("修改后的数组：")
    print(np.ceil(a))




