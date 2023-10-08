{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import boto3\
import json\
\
def lambda_handler(event, context):\
    \
    text = event['input'];\
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-2\'92)\
    phrases = comprehend.detect_key_phrases(Text=text, LanguageCode='en')\
   \
    return \{\
        'statusCode': 200,\
        'body': \{ 'KeyPhrases' : phrases['KeyPhrases']\}\
    \}\
}