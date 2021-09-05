import boto3

client = boto3.client('ec2')
client.delete_vpc(VpcId='vpc_ID')