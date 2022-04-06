import matplotlib.pyplot as plt			                     # 引入matplotlib模块并简化
import torch                                                 # 引入torch模块
import numpy as np                                           # 引入numpy模块
x = torch.linspace(-np.pi, np.pi, 100)						 # 设置每个点的x坐标
plt.ion()                                                    # 打开交互模式
for i in range(50)                                          # 循环50次
    plt.cla()                                                # 清除上一次绘图
    y = np.sin(x) + torch.rand(x.size())			         # 设置每个点的y坐标，添加随机数
    plt.scatter(x, y)                                        # 绘制散点图
    plt.pause(0.1)                                           # 显示时间0.1秒
plt.ioff()                                                   # 关闭交互模式
plt.show()							                         # 定格显示最后一张图