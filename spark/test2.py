import sys
from operator import add

from pyspark import SparkContext
from pyspark import SparkConf

logFile = "C:\Users\simon\Desktop\word.txt"

# conf =SparkConf().setAppName("test").setMaster("local")
# sc = SparkContext(conf)
sc = SparkContext("local", "PythonWordCount")

logData = sc.textFile(logFile)
print(logData.count())

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))