import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline
a = [1, 2, 4]
b = [4, 5, 6]

c = [10, 12, 14]
d = [14, 15, 16]
#plt.plot(a, b)  # 画线a=x坐标，b=y坐标
#plt.plot(a, b, '*')# 画*的点 a=x坐标，b=y坐标
#plt.plot(a, b, 'r--')# 画红色曲线 a=x坐标，b=y坐标


#plt.plot(a, b ,'r--', c,d, 'b*', label='xxx')
plt.plot(a, b ,'r--', label='xxx')#线段名字
plt.xlabel('this is x label')#x轴名字
plt.ylabel('this is y label')#y轴名字
plt.title('title')
plt.show()
