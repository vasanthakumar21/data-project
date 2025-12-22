df = spark.read.option("header", True).csv(
    "s3://kaggle-raw-bucket/input/"
)

clean_df = df.dropna().dropDuplicates()

clean_df.write.mode("overwrite").parquet(
    "s3://kaggle-clean-bucket/processed/"
)
