from pyspark.sql import *
from pyspark import SparkFiles
#from pyspark import SparkContext as sc
from pyspark import SparkConf
from pyspark.context import SparkContext



if __name__ == "__main__":
    
    
    spark = SparkSession.builder \
            .appName("Micro Project") \
            .master("local[2]") \
            .getOrCreate()
        
    sc = SparkContext.getOrCreate(SparkConf())

    """ 
    ## Works:
    data_file_https_url = "https://gist.githubusercontent.com/aakashjainiitg/dbb668c58839d68d7903f508bf55043c/raw/1feec07802b4f53aceac450fa1aee5a87d9276e0/cities_data_bank.csv"
    sc.addFile(data_file_https_url)
    filePath  = 'file://' +SparkFiles.get('cities_data_bank.csv')
    print("Filepath:" + filePath)
    citiesDf = spark.read.csv(filePath, header=True, inferSchema= True)
    citiesDf.show()
    """
  
    path = "/workspaces/Studying-Spark/nuek-vuh3.csv"

    sc.addFile(path)
    df = spark.read.csv(path, header=True, inferSchema= True)
    df.show()

   