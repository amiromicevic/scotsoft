import boto3
import json
import base64
import numpy as np

def lambda_handler(event, context):
    
    input = event['input']
    endpoint_name = ‘END POINT NAME GOES HERE’
   
    payload = {"prompt":input, "width":312, "height":312}
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=json.dumps(payload).encode('utf-8'), Accept = 'application/json;jpeg')
    
    response_dict = json.loads(response['Body'].read())
    generated_image = response_dict['generated_images']
   
    return {
        'statusCode': 200,
        'body': {
            'header':'data:image/jpeg;base64,',
            'base64':response_dict['generated_images']
        }
    }
