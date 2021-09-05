import boto3
import pprint

s3_resource = boto3.client('s3')

objects = s3_resource.list_objects(Bucket='BucketName')['Contents']
pprint(objects)
print(len(objects))