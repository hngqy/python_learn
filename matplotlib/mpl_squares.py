# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

input_value=[1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_value,squares,linewidth=10)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squares Numbers Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
#plt.show()

print plt.__doc__