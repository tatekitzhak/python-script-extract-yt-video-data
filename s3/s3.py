import boto3
import os
from dotenv import load_dotenv
load_dotenv()


S3_ACCESS_KEY =  os.getenv("S3AccessKeyID")
s3_SECRET_KEY =  os.getenv("S3SecretAccessKey")

s3 = boto3.resource('s3',aws_access_key_id=S3_ACCESS_KEY,aws_secret_access_key=s3_SECRET_KEY)

for each_bucket in s3.buckets.all():
	print('s3:',each_bucket.name)


