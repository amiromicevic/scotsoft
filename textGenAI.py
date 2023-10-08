{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww20320\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
import boto3\
\
def lambda_handler(event, context):\
    \
    input = event['input']\
    endpoint_name = \'91END \'91POINT NAME GOES HERE\'92\
   \
    payload = \{\
        "inputs": input,\
        "parameters":\{\
            # "max_new_tokens": 180,\
            "max_new_tokens": 130,\
            "return_full_text": False,\
            "do_sample": True,\
            "top_k":10\
        \}\
    \}\
    \
    client = boto3.client('runtime.sagemaker')\
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=json.dumps(payload).encode('utf-8'))\
    model_predictions = json.loads(response['Body'].read())\
    generated_text = model_predictions[0]['generated_text']\
\
    return \{\
        'statusCode': 200,\
        'body': json.dumps(generated_text)\
    \}\
}