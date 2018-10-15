import  matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0)
y1 = np.sin(np.pi*x)
y2 = np.sin(np.pi*x*2)
'''
plt.plot(x, y1, 'b--', label='sin(pi*x)')
plt.ylabel('y1-value')
plt.plot(x, y2, 'r--', label='sin(pi*x*2)')
plt.ylabel('y2-value')
plt.xlabel('x-value')
plt.title('titile')
plt.legend()
plt.show()
'''
'''
#分2个图显示..2行1列
plt.subplot(2, 1, 1)#plt.subplot(211)也可以
plt.plot(x, y1, 'b--')
plt.ylabel('y1')
plt.subplot(2, 1, 2)
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.xlabel('x')
plt.show()

figure, ax = plt.subplots()#分2个对象，一个是图框，一个是图
ax.plot([1,2,3,4])
plt.show()
'''
figure, ax = plt.subplots(2,2)
ax[0][0].plot([1,2,3,4])
plt.show()
