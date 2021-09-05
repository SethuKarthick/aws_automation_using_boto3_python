import boto3

client = boto3.client('ec2')

client.revoke_security_group_egress(
    GroupId='security_grp_Id',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
               {
                    'CidrIp': '0.0.0.0/0',
                    'Description': '_existing_description'
                },
            ],
            'ToPort': 80,
        },
    ],
)