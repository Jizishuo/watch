import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    np.random.randint(1,10,40).reshape(10, 4), #1-10取40个
    columns=['A','B','C','D']
)
'''
df.plot(kind='area')
#.plot(xxx) 很多参数
# kind=line/bar/barch/hist/box/kde/density/area/pie
#stacked = True                         #柱状图叠在一起(bar)堆叠
#grid = True/False                      #背景是否有方格
#label='s1'                             #图例名称
#title = 'sss'                          #图名称
#style='--'                             #线段样子--虚线
plt.legend()                            #显示图例
plt.show()
'''
#每行画图 ( 默认是列画图) df.T.plot()
for i in df.index:
    df.iloc[i].plot(labels=str(i))
plt.legend()
plt.show()