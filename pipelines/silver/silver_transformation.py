from pyspark.sql.functions import col
from pyspark.sql.functions import year

from utils.spark_session import get_spark


def silver_transformation():

    spark = get_spark()

    df = spark.read.parquet("data/bronze/yellow_tripdata")

    # Remove duplicate rows
    df = df.dropDuplicates()

    # Remove rows with null pickup datetime
    df = df.filter(col("tpep_pickup_datetime").isNotNull())

    # Remove negative fares
    df = df.filter(col("fare_amount") >= 0)

    # Remove negative distance
    df = df.filter(col("trip_distance") >= 0)
    
    df = df.filter(year("tpep_pickup_datetime") == 2021)
    
    print("Silver Record Count:", df.count())
    print("=" * 50)

    df.show(5, truncate=False)

    (
        df.write
        .mode("overwrite")
        .parquet("data/silver/yellow_tripdata")
    )

    print("Silver Layer Created Successfully")

    spark.stop()


if __name__ == "__main__":
    silver_transformation()