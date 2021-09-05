import boto3

ec2_client = boto3.client("ec2")

ec2_client.detach_volume(InstanceId="String ID on Instance", 
                        VolumeId="String Volume ID")