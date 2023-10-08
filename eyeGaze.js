import * as AWS from "/opt/nodejs/node_modules/@aws-sdk/client-rekognition/dist-cjs/index.js";
const client = new AWS.Rekognition();
    
export const handler = async (event, context) => {

    const response = {
        isBase64Encoded: false,
        body: null,
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
        //version: AWS.version,
        statusCode: 200
    };

    const base64Image = event.body;

    // Convert to buffer
    const decodedImage = Buffer.from(base64Image, 'base64');

    const params = {
        Attributes: ["EYE_DIRECTION"],
        Image: {
            Bytes: decodedImage,
        },
    };

    const command = new AWS.DetectFacesCommand(params);
    const recognitionResponse = await client.send(command);
    response.body = recognitionResponse.FaceDetails[0].EyeDirection;
    
    return response;
};

