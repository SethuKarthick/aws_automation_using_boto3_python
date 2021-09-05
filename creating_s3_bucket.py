import boto3
import pprint

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("test-25-07")

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },
)

pprint(response)