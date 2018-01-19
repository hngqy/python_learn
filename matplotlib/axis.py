import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3],[4,5,6])
axis = plt.gca().xaxis
plt.show()

print axis.get_ticklocs()

for x in axis.get_ticklabels():
    print x.get_text()

for y in axis.get_ticklines():
    print y.get_text()


