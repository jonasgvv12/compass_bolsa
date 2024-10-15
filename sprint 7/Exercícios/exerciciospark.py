from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Contador de Palavras") \
    .getOrCreate()

sc = spark.sparkContext

text_file = sc.textFile("/home/jovyan/work/readme.md")

words = text_file.flatMap(lambda line: line.split(" "))

word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

word_counts.collect()

spark.stop()