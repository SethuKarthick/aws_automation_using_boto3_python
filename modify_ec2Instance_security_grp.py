import boto3

ec2_client = boto3.client("ec2")

ec2_client.modify_instance_attribute(InstanceId="String_InstanceID", 
                                     Groups=[
                                        "string_security_grp_id"
                                     ]
)