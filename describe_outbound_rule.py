import boto3

client = boto3.client('ec2')
client.update.security_group_rule_description.egress(
    GroupId='security_grp_Id',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': '_Change_description'
                },
            ],
            'ToPort': 80,
        },
    ],
)