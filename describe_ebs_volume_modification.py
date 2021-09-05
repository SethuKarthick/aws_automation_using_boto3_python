import boto3

ec2_client = boto3.client("ec2")

ec2_client.describe_volumes_modifications(VolumeIds=[
    'string_volumeId'
])