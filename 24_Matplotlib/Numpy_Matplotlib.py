"""
描述：Numpy-Matplotlib绘图
参考：https://www.runoob.com/numpy/numpy-matplotlib.html
作者：王佳秋
日期：2020年7月29日
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


if __name__ == "__main__":

    # 1.实例1
    x = np.arange(1, 11)
    print("x:", x)
    y = 2 * x + 5
    print("y:", y)
    plt.title("Matplotlib demo")
    plt.xlabel('x axis caption')
    plt.ylabel('y axis caption')
    plt.plot(x, y)
    plt.show()

    """图形中文显示"""
    # fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
    zhfont1 = font_manager.FontProperties(fname="D:\Downloads\SourceHanSansSC-Bold.otf")
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)
    # fontproperties设置中文显示，fontsize设置字体大小
    plt.xlabel("x 轴", fontproperties=zhfont1)
    plt.ylabel("y 轴", fontproperties=zhfont1)
    plt.plot(x, y)
    plt.show()

    # 此外，我们还可以使用系统的字体：
    a = sorted([f.name for f in font_manager.fontManager.ttflist])
    for i in a:
        print("系统字体：", i)
    """印出你的 font_manager 的 ttflist 中所有注册的名字，找一个看中文字体例如：STFangsong(仿宋）,然后添加以下代码即可："""
    plt.rcParams['font.family'] = ['STFangsong']

    # 2. 实例
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y, "ob")
    plt.show()

    """绘制正弦波"""
    # 计算正弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sine wave form")
    # 使用 matplotlib 来绘制点
    plt.plot(x, y)
    plt.show()

    """subplot() 函数允许你在同一图中绘制不同的东西。"""
    # 以下实例绘制正弦和余弦值:
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # 建立 subplot 网格，高为 2，宽为 1
    # 激活第一个 subplot
    plt.subplot(2, 1, 1)
    # 绘制第一个图像
    plt.plot(x, y_sin)
    plt.title('Sine')
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title("Cosine")
    # 展示图形
    plt.show()

    """bar(): pyplot 子模块提供 bar() 函数来生成条形图。"""
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

    """numpy.histogram() 函数是数据的频率分布的图形表示。 """
    a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
    hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
    print(hist)
    print(bins)
    plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
    plt.title("histogram")
    plt.show()




