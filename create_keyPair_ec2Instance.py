import boto3
import io

ec2_client = boto3.client("ec2")

key_pair = ec2_client.create_key_pair(KeyName="string_")

key_data = key_pair["KeyMaterial"]

with io.open("tutu.pem", 'w' , encoding='utf-8') as f1:
    f1.write(str(key_data))
    f1.close
