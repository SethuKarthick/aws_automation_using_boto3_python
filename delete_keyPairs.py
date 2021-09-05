import boto3

ec2_client =  boto3.client("ec2")

data = ec2_client.describe_key_pairs()

key_data = data["KeyPairs"]

for key in key_data:
    name = key["KeyName"]
    ec2_client.delete_key_pair(KayName=name)