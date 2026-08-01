from pyspark.sql import SparkSession


def get_spark():
    spark = (
        SparkSession.builder
        .appName("Lakehouse Platform")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark