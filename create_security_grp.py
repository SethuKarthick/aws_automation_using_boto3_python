import boto3

client = boto3.client('ec2')
client.create_security_group(Description='description', GroupName='preferredName' )

# associate security grp with specific vpc
client.create_security_group(Description='description', GroupName='preferredName', VpcId='vpcId' )