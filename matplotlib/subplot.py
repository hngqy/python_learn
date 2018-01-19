import matplotlib.pyplot as plt
import numpy as np

for idx,color in enumerate("rgbyck"):
    plt.subplot(320+idx+1,axisbg=color)

plt.show()