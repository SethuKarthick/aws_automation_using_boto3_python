import boto3

ec2_client = boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone="Should be same as instance zone", 
                         #Encrypted=True|False,
                         #Iops=123,
                         #KmsKeyId="string", 
                         #OutpostArn="String",
                         Size=123,
                         SnapshotId="String", 
                         VolumeType= "standard"|"io1"|"gp2"|"ac1"|"st1",
                         TagSpecification=[{
                            'ResourceType' :'volume',
                            'Tags':[{
                                "Key":"Name",
                                "Value":"test"
                            },]
                         },])

ec2_client.delete_volume(VolumeId="string")