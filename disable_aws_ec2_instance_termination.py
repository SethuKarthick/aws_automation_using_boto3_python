from logging import disable
import boto3

ec2_client = boto3.client("ec2")

ec2_client.modify_instance_attribute(InstanceId = "String_instance_ID", 
                                     DisableApiTermination={
                                         "Value" : True|False
                                     })