import boto3

s3_resource = boto3.client('s3')
# to download single file 
s3_resource.download_file(Bucket='BucketName', Key='KeyName', Filename="directory")

import os 

cwd = os.getcwd()

cwd = cwd+"/downloads/"

files = s3_resource.list_objects(Bucket='BucketName')['Contents']

for file in files:
    s3_resource.download_file(Bucket='BucketName', Key=file["Key"], Filename=cwd+'download_'+file['Key'])