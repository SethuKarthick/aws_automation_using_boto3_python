import boto3

s3_resource = boto3.client('s3')

# to upload single file
s3_resource.upload_file(Filename='upload.png', Bucket='bucketName', Key='uploadtest.png')

# to upload multiple files 

import os 
import glob 

cwd = os.getcwd()

files = cwd+'/folder/*'

for file in files:
    s3_resource.upload_file(Filename=file, Bucket='BucketName', Key=file.split('/')[-1])