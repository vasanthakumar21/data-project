df = spark.read.option("header", True).csv(
    "s3://kaggle-raw-bucket-vas/input/"
)

clean_df = df.dropna().dropDuplicates()

clean_df.write.mode("overwrite").parquet(
    "s3://kaggle-clean-bucket-vas/processed/"
)
