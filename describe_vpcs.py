import boto3
from pkg_resources import normalize_path

client = boto3.client('ec2')

x = client.describe_vpcs()

print(x['Vpcs'])

no_of_vpcs = x['Vpcs']

for vpc in no_of_vpcs:
    print(vpc['VpcId'])
    
x= client.describe_vpcs(VpcIds=['VpcId'])