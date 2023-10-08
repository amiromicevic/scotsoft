{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import * as AWS from "/opt/nodejs/node_modules/@aws-sdk/client-rekognition/dist-cjs/index.js";\
const client = new AWS.Rekognition();\
    \
export const handler = async (event, context) => \{\
\
    const response = \{\
        isBase64Encoded: false,\
        body: null,\
        headers: \{\
            'Access-Control-Allow-Origin': '*',\
        \},\
        //version: AWS.version,\
        statusCode: 200\
    \};\
\
    const base64Image = event.body;\
\
    // Convert to buffer\
    const decodedImage = Buffer.from(base64Image, 'base64');\
\
    const params = \{\
        Attributes: ["EYE_DIRECTION"],\
        Image: \{\
            Bytes: decodedImage,\
        \},\
    \};\
\
    const command = new AWS.DetectFacesCommand(params);\
    const recognitionResponse = await client.send(command);\
    response.body = recognitionResponse.FaceDetails[0].EyeDirection;\
    \
    return response;\
\};\
\
}