from pyspark.sql.functions import current_timestamp, lit

from utils.spark_session import get_spark


def bronze_ingestion():
    spark = get_spark()

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("data/raw/yellow_tripdata_2021-01.csv")
    )

    # Add audit columns
    df = (
        df.withColumn("ingestion_timestamp", current_timestamp())
          .withColumn("data_source", lit("NYC Taxi"))
    )

    print("=" * 50)
    print("Raw Record Count:", df.count())
    print("=" * 50)

    df.printSchema()

    df.show(5, truncate=False)

    (
        df.write
        .mode("overwrite")
        .parquet("data/bronze/yellow_tripdata")
    )

    print("Bronze Layer Created Successfully")

    spark.stop()


if __name__ == "__main__":
    bronze_ingestion()