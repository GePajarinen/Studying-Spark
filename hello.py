from pyspark.sql import *

if __name__ == "__main__":
    
    spark = SparkSession.builder \
        .appName("Spark 1") \
        .master("local[2]") \
        .getOrCreate()
    
    data_list = [("Carla", 28),
                ("Mara", 33),
                ("Marcos", 44)]
    
    df = spark.createDataFrame(data_list).toDF("name", "age")
    df.show()