import boto3

ec2_client = boto3.client("ec2")

data = ec2_client.describe_key_pairs()

data = data["KeyPairs"] 

for key in data:
    key["KeyPairId"]