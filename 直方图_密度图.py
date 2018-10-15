import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s1 = pd.Series(np.random.randn(1000))
'''
#直方图分布情况
plt.hist(s1, rwidth=0.9, bins=20, color='r') #间隔宽度, 分成20份
plt.show()
'''

s1.plot(kind='kde') #密度图
plt.show()