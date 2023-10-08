import boto3
import json

def lambda_handler(event, context):
    
    text = event['input'];
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-2’)
    phrases = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
   
    return {
        'statusCode': 200,
        'body': { 'KeyPhrases' : phrases['KeyPhrases']}
    }
