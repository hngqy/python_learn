import pickle as pl

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data2.pkl', 'wb')

# Pickle dictionary using protocol 0.
#pickle.dump(data1, output)

pl.dump()
# Pickle the list using the highest protocol available.
pl.dump(selfref_list, output, -1)

output.close()