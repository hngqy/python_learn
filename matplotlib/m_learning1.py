# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,5,0.1)
print x
y=np.sin(x)
print y

plt.plot(x,y)
plt.title("sin值")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

