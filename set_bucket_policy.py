import boto3
import json

s3_resource = boto3.client('s3')

bucket_policy =  #json_value

bucket_policy = json.dump(bucket_policy)

s3_resource.put_bucket_policy(Bucket='bucketname', Policy='Bucket_policy') 

