import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("rekognition")

    if "Records" in event and len(event["Records"]) > 0:
        record = event["Records"][0]
        if "s3" in record and "bucket" in record["s3"] and "object" in record["s3"]:
            file_bucket = record["s3"]["bucket"]["name"]
            file_key = record["s3"]["object"]["key"]

            response = client.detect_labels(Image={"S3Object": {"Bucket": file_bucket, "Name": file_key}}, MaxLabels=5, MinConfidence=70)
            print(response)

            # Extract the detected labels from the response
            labels = [label['Name'] for label in response['Labels']]

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Image processed successfully!', 'labels': labels})
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid S3 event structure!')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid Lambda event structure!')
        }