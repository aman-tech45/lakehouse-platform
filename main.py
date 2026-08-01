from utils.spark_session import get_spark

spark = get_spark()

print("=" * 50)
print("Lakehouse Platform Started")
print(f"Spark Version: {spark.version}")
print("=" * 50)

spark.stop()