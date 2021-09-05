import boto3

ec2_client = boto3.client("ec2")

ec2_client.stop_instances(InstanceIds=["string_instanceIds"])
ec2_client.modify_instance_attribute(InstanceId = "String_instanceID",
                                     InstanceType = {
                                         "Value" : "t2.nano"
                                     })