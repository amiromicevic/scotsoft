import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3'
import { getSignedUrl } from '@aws-sdk/s3-request-presigner'
import { PollyClient, SynthesizeSpeechCommand } from "@aws-sdk/client-polly";
import { Upload } from '@aws-sdk/lib-storage';

export const handler = async (event) => {
  
  let text = event.text;
  let bucket = event.bucket;
  let key = event.key;
  
  const s3Client = new S3Client();
  const s3Command = new GetObjectCommand({
    Bucket: "speech-to-sound-polly",
    Key: key
  });

  const preSignedUrl = await getSignedUrl(s3Client, s3Command, {
    expiresIn: 600
  });

  const pollyClient = new PollyClient({ region: "eu-west-2" });
  
  const params = {
    Engine: "neural",
    OutputFormat: "mp3",
    Text: text,
    TextType: "text",
    VoiceId: "Amy",
    SampleRate: "24000",
  };

  const pollyCommand = new SynthesizeSpeechCommand(params);
  const pollyResponse = await pollyClient.send(pollyCommand);
  
  const s3Params = {
    Bucket: "speech-to-sound-polly",
    Key: key ,
    Body: pollyResponse.AudioStream
  };
  
 const upload = new Upload({
    client: s3Client,
    params: s3Params,
    queueSize: 4, // optional concurrency configuration
    partSize: 1024 * 1024 * 5, // optional size of each part, in bytes, at least 5MB
    leavePartsOnError: false // optional manually handle dropped parts
  });
  
  await upload.done();
  
  const response = {
    statusCode: 200,
    body: { 'preSignedUrl': preSignedUrl},
  };
  
  return response;
};



