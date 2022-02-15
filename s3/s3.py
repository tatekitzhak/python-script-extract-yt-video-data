import boto3

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')
iam = boto3.resource('iam')

for each_bucket in s3.buckets.all():
	print('s3:',each_bucket)