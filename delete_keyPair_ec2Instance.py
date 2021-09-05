import boto3

ec2_client = boto3.client("ec2")

ec2_client.delete_key_pair(KeyName="String_")