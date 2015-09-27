from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("spark_app_fullOuterJoin")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([("a", 1), ("b", 1)])

rdd2 = sc.parallelize([("a", 2), ("c", 1)])

datas = rdd1.fullOuterJoin(rdd2).collect()

sc.stop()

print datas
