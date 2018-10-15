import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s1 = pd.Series(np.random.randn(1000).cumsum())
s2 = pd.Series(np.random.randn(1000).cumsum())
#s = pd.Series([1,2,3,4,5])
'''
s1.plot()
s2.plot()
#s1.plot(xxx) 很多参数
# kind=line/bar/barch/hist/box/kde/density/area/pie
#grid = True/False                      #背景是否有方格
#label='s1'                             #图例名称
#title = 'sss'                          #图名称
#style='--'                             #线段样子--虚线
plt.legend()                            #显示图例

plt.show()
'''
'''
fig, ax = plt.subplots(2, 1)
ax[0].plot(s1)
ax[1].plot(s2)
plt.show()
'''

fig, ax = plt.subplots(2, 1)
s1[0:10].plot(ax=ax[0], kind='bar')
s2[0:10].plot(ax=ax[1], kind='bar')
plt.show()