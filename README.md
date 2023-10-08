# scotsoft
Reference material from Scotsoft presentation
The following lambda files represent simple backend functionality that support the features presented on the demo at ScotSoft 2023.

**Comprehend.py** takes a text paragraph and requests Amazon Comprehend service to run insight analysis on the text and extract the key phrases and return them to the front end.

**EyeGaze.js** takes the still image from the front end which is passed to the function as base64 encoded string. The string is decoded to an array of bytes and passed to Amazon Rekognition service to run DetectFaces command to detect the face on the still image, and then extract key insights from the face, including EyeDirection parameter. The resulting json is then returned to the front end.

**ImageGenAI.py** connects to the provisioned inference end point created by Amazon SageMaker JumpStart and passes the prompt with the instructions for image creation to the foundational model. The generated image is then returned to the front end as the base64 encoded jpeg.

**Sound.js** takes text as input as converts it into sound that is saved to your designated S3 bucket, and is played by the front end via JavaScript that downloads the sound file from the S3 bucket. Lambda function creates a presigned Url that acts as as a temporary permission that allows the authorised users to download the audio file from the bucket. The function uses Amazon Polly service to convert text to sound, and the resulting audio strsam is saved to the designated S3 bucket. The presigned Url is then returned to the front end and it allows user to access and download the saved sound file, and no more than that.

**TexctGenAI.py** connects to the provisioned inference end point created by Amazon SageMaker JumpStart and passes the prompt with the instructions for text creation to the foundational model. The generated text is then returned to the front end.
