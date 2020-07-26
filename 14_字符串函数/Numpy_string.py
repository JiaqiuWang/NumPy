"""
描述：Numpy-字符串函数
参考：https://www.runoob.com/numpy/numpy-string-functions.html
作者：王佳秋
日期：2020年7月26日
"""


import numpy as np


if __name__ == "__main__":

    # 1.numpy.char.add()依次对两个数组的元素进行字符串连接
    print("连接两个字符串：", np.char.add(['hello'], ['xyz']), "\n")
    print("连接示例：")
    print(np.char.add(['hello', 'hi'], ['abc', 'xyz']))

    # 2.numpy.char.center()用于将字符串居中，并使用指定字符串在左侧和右侧进行填充
    # np.char.center(str, width, fillchar)
    # str: 字符串，width: 长度，fillchar: 填充字符
    print(np.char.center('Runoob', 20, fillchar="*"))

    # 3.numpy.char.capitalize()将字符串的第一个字母转换为大写
    print(np.char.capitalize('runoob hello'))

    # 4.numpy.char.title()将字符串中每个单词的第一个字母转换为大写
    print(np.char.title('i like runoob.'))

    # 5.numpy.char.lower()对数组中每个元素转换为小写，对每个元素调用str.lower
    # 5.1 操作数组
    print(np.char.lower(['RUNOOB', 'GOOGLE']))
    # 5.2 操作字符串
    print(np.char.lower('WANG JIAQIU'))

    # 6.numpy.char.upper()对数组中每个元素转换为大写，它对每个元素调用str.upper
    # 6.1 操作数组
    print(np.char.upper(['runoob', 'google']))
    # 6.2 操作字符串
    print(np.char.upper('wang jiaqiu'))

    # 7.numpy.char.split()通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
    # 7.1 分隔符为空格
    print(np.char.split('i like runoob?'))
    # 7.2 分隔符为 .
    print(np.char.split('www.runoob.com', '.'))

    # 8.numpy.char.splitlines()以换行符为分隔符来分割字符串，并返回数组
    # \n, \r, \r\n 都可以作换行符
    print(np.char.splitlines('i\nlike runoob?'))
    print(np.char.splitlines('i\rlike runoob?'))

    # 9.numpy.char.strip()移除开头或结尾处的特定字符
    # 9.1 移除字符串头尾的 a 字符
    print(np.char.strip('ashok arunooba', 'a'))
    # 9.2 移除数组中各元素头尾的 a 字符
    print(np.char.strip(['arunooba', 'admaina', 'java'], 'a'))

    # 10.numpy.char.join()通过指定分隔符来连接数组中元素或字符串
    # 10.1 操作字符串
    print(np.char.join(':', 'runoob'))
    # 10.2 指定多个分隔符操作数组
    print(np.char.join([':', '-'], ['runoob', 'google']))
    print(np.char.join([':', '-'], ['runoob']))

    # 11.numpy.char.replace()使用新字符串替换原字符串中所有子字符串
    print(np.char.replace('i like runoob', 'oo', 'cc'))

    # 12.numpy.char.encode()对数组中的每个元素调用str.encode()
    a = np.char.encode('runoob', 'cp500')
    print("a:", a)

    # 13.numpy.char.decode()对编码的元素进行str.decode()解码
    print("解码：", np.char.decode(a, 'cp500'))
