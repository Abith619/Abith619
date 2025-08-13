from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("MyApp").getOrCreate()

sc = spark.sparkContext
print("Spark Version:", sc.version)

csv_df = spark.read.csv("F:/pyspark/archive/spotify_history.csv", header=True, inferSchema=True)

sorted_df = csv_df.orderBy("ms_played", ascending=False).limit(20)
sorted_df.show()
