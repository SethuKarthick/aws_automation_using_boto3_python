import boto3

client = boto3.client('ec2')

client.delete_security_group(GroupId='security_grp_Id')