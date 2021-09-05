import boto3

client = boto3.client("ec2")

x = client.describe_security_groups()

security_grps = x["SecurityGroups"]

for grp in security_grps:
    print(grp['GroupId'])
    
x = client.describe_security_groups(GroupIds=['groupsId'])

# using filters

x = client.describe_security_groups(Filters=[
    {
        'Name': 'grp-Name/grp-Id',
        'Values': [
            'security-grp-name',
            'default'
        ]
    },
],) 