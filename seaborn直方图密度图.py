import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s1 = pd.Series(np.random.randn(1000))
#plt.hist(s1)

#s1.plot(kind='kde')
#plt.show()

sns.distplot(s1, bins=20, hist=True, kde=True, rug=True)
plt.show()