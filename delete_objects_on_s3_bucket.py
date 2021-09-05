import boto3
from botocore.retries import bucket

s3_resource = boto3.client('s3')

# to delete single object
s3_resource.delete_object(Bucket='bucketName', Key='FileKeyName.png')

# to delete multiple objects
 
objects = s3_resource.list_objects(Bucket='bucketName')['Contents']

for object in objects:
    s3_resource.delete_object(Bucket='bucketName', Key=object['Key'])
