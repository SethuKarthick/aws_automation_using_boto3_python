import boto3

ec2_resource = boto3.resource('ec2')
ec2_resource.create_instance(
    ImageId='String/image_ID', InstanceType = 't2_micro', MaxCount=1, MinCount=1)