import pandas as pd
import numpy as np


s = pd.Series(np.array([1,3,5,np.nan,np.nan,6,8]))
print s
datets = pd.date_range('20130101',periods=6)
print datets

df = pd.DataFrame(np.random.randn(6,4),index=datets,columns=list('ABCD'))
print df

pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':pd.ar
})