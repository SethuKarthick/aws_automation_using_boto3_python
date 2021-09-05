import boto3

ec2_client = boto3.client("ec2")

response = ec2_client.describe_volume()
data = response["Volumes"]
for volume in data:
    print(volume)