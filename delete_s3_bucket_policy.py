import boto3
from botocore.retries import bucket

s3_resource = boto3.client('s3')

s3_resource.delete_bucket_policy(Bucket='bucketName')