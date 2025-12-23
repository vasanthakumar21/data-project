import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Arguments passed from Lambda
args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME', 'input_bucket', 'input_key']
)

input_bucket = args['input_bucket']
input_key = args['input_key']

input_path = f"s3://{input_bucket}/{input_key}"
output_path = "s3://kaggle-clean-bucket-vas/processed/"

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 🔹 Read CSV from S3
df = spark.read.option("header", "true").csv(input_path)

# 🔹 Simple cleaning
clean_df = df.dropna().dropDuplicates()

# 🔹 Write to S3 (folder auto-created)
clean_df.write.mode("overwrite").parquet(output_path)

job.commit()
