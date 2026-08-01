from pyspark.sql.functions import (
    count,
    sum,
    avg,
    date_format,
    round
)

from utils.spark_session import get_spark


def gold_aggregation():

    spark = get_spark()

    df = spark.read.parquet("data/silver/yellow_tripdata")

    # Monthly Business KPIs
    monthly_summary = (
        df.groupBy(
            date_format("tpep_pickup_datetime", "yyyy-MM").alias("month")
        )
        .agg(
            count("*").alias("total_trips"),
            round(sum("fare_amount"), 2).alias("total_revenue"),
            round(avg("fare_amount"), 2).alias("average_fare"),
            round(avg("trip_distance"), 2).alias("average_distance")
        )
    )

    monthly_summary.show(truncate=False)

    (
        monthly_summary.write
        .mode("overwrite")
        .parquet("data/gold/monthly_summary")
    )

    print("Gold Layer Created Successfully")

    spark.stop()


if __name__ == "__main__":
    gold_aggregation()