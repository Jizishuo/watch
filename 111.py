import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#中文显示设置字体
'''font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 'larger'}
matplotlib.rc('font', **font)'''

#from matplotlib import font_manager
#my_fount = font_manager.FontProperties(fname='字体的路径')#很多参数看源码size----


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

#设置大小 和像素
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x, y)
x_zhou = [i/2 for i in range(2,24)]
#plt.xticks(range(2, 25)) #x的坐标轴
x_labels = ['hellow,{}'.format(i) for i in x]
plt.xticks(x, x_labels, rotation=90) #x和x_labels长度要一样 rotation x轴刻度旋转
#plt.savefig('路径') #保存
plt.show()