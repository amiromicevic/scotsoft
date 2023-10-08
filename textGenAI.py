import json
import boto3

def lambda_handler(event, context):
    
    input = event['input']
    endpoint_name = ‘END ‘POINT NAME GOES HERE’
   
    payload = {
        "inputs": input,
        "parameters":{
            # "max_new_tokens": 180,
            "max_new_tokens": 130,
            "return_full_text": False,
            "do_sample": True,
            "top_k":10
        }
    }
    
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=json.dumps(payload).encode('utf-8'))
    model_predictions = json.loads(response['Body'].read())
    generated_text = model_predictions[0]['generated_text']

    return {
        'statusCode': 200,
        'body': json.dumps(generated_text)
    }
