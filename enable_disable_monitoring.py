import boto3

ec2_client = boto3.client("ec2")

# to enable monitoring 
ec2_client.monitor_instances(InstanceIds =['Id_of_instances'])

# to disable monitoring 
ec2_client.unmonitor_instances(InstanceIds =['Id_of_instances'])