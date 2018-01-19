import datetime
import os

path=os.getcwd()
flag = os.path.exists(path+"/test.txt")
print flag
if flag:
    file = open('test.txt', 'r')
    for line in file:
        print line
else:
    file = open('test.txt', 'a')
    file.writelines("aaaaa\n")
    file.writelines("bbbbb\n")
    file.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

with open('test1.txt','w') as wfile:
    wfile.write('bbb')
"""
file=open('test.txt','w')
file.writelines("aaaaa\n")
file.writelines("bbbbb\n")
file.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
"""


