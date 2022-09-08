import json
import base64
import os
import boto3
from urllib.request import urlopen
import datetime

def lambda_handler(event, handler):
    # TODO implement
    print("INN")
    image = base64.b64encode(urlopen("https://dockercontainer2.s3.ap-south-1.amazonaws.com/SampleVideo_720x480_5mb.mp4").read())
    print(image)
    
    s3_client = boto3.client('s3')
    s3_client.put_object(ACL='public-read',Body=image, Bucket='dockercontainer2', Key='sample')
    
    print("INNSIDE")
    return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
}
