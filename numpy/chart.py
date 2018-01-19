import numpy as np


np.genformtxt( )
# read the first 4 columns
data = np.genfromtxt('iris.csv',delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = np.genfromtxt('iris.csv',delimiter=',',usecols=(4),dtype=str)