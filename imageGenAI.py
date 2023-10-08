{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import boto3\
import json\
import base64\
import numpy as np\
\
def lambda_handler(event, context):\
    \
    input = event['input']\
    endpoint_name = \'91END POINT NAME GOES HERE\'92\
   \
    payload = \{"prompt":input, "width":312, "height":312\}\
    client = boto3.client('runtime.sagemaker')\
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=json.dumps(payload).encode('utf-8'), Accept = 'application/json;jpeg')\
    \
    response_dict = json.loads(response['Body'].read())\
    generated_image = response_dict['generated_images']\
   \
    return \{\
        'statusCode': 200,\
        'body': \{\
            'header':'data:image/jpeg;base64,',\
            'base64':response_dict['generated_images']\
        \}\
    \}\
}