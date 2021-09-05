import boto3

client = boto3.client('ec2')
client.authorize_security_group_ingress(
    GroupId='security_grp_Id',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'description'
                },
            ],
            'ToPort': 80,
        },
    ],
)