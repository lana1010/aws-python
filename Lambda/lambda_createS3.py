###############################################
#
# Creating AWS S3 bucket by Lambda Function
#
###############################################

import boto3, os, time

AWS_DAFAULT_REGION = "eu-west-1"   #Region where lambda running
os.environ['AWS_DAFAULT_REGION'] = AWS_DAFAULT_REGION

def lambda_handler(event, context):
    bucket_name = "s3.created.by.lambda-" + str(time.time())
    
    # Create an S3 client
    s3 = boto3.client('s3')
    
    try:
        # Create the S3 bucket
        s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': AWS_DAFAULT_REGION})
        response = {
            'statusCode': 200,
            'body': f'Successfully created S3 bucket: {bucket_name}'
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': f'Error creating S3 bucket: {bucket_name}. Reason: {str(e)}'
        }
    
    return response