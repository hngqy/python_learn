import os
import sys
# Path for spark source folder
os.environ['SPARK_HOME'] = "C:\DEV\tool\spark-1.6.1-bin-hadoop2.6"

# Append pyspark to Python Path
sys.path.append("C:\DEV\tool\spark-1.6.1-bin-hadoop2.6\python")
# sys.path.append("C:\DEV\tool\spark-1.6.1-bin-hadoop2.6\python\lib\py4j-0.9-src.zip")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print("Successfully imported Spark Modules")
    sc = SparkContext("local", "test")
    rdd = sc.textFile("C:\Users\simon\Desktop\word.txt")
    print "rdd.count():%s", str(rdd.count())

except ImportError as e:
    print("Can not import Spark Modules", e)
sys.exit(1)