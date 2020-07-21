"""
描述：Numpy-dtype数据类型
参考：https://www.runoob.com/numpy/numpy-dtype.html
作者：王佳秋
日期：2020年7月19日
"""


import numpy as np


if __name__ == "__main__":

    # 1.使用标量类型
    dt = np.dtype(np.int32)
    print("1.使用标量类型：", dt)

    # 2.int8, int16, int32, int64 四种数据类型可以使用字符串'i1', 'i2', 'i4', 'i8'代替
    dt = np.dtype('i4')
    print(dt)

    # 3.字节顺序标注
    dt = np.dtype('<i4')
    print("字节顺记标注: ", dt)

    # 4.创建结构化数据类型
    dt = np.dtype([('age', np.int8)])
    print("创建结构化数据类型：", dt)

    # 5.将数据类型应用于ndarray对象
    dt = np.dtype([('age', np.int8)])
    a = np.array([(10, ), (20, ), (30, )], dtype=dt)
    print("将数据类型应用于ndarray对象：", a)

    # 6.类型字段名可以用于存取实际的age列
    dt = np.dtype([('age', np.int8)])
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print("类型字段名可用于存取实际的age列：", a['age'])

    # 7.定义一个结构化数据类型
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print(student)

    # 8.
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    print("自定义数据类型的数据：", a)
