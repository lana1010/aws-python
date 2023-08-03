###########################################
#
# List all AWS S3 buckets by Lambda
#
###########################################

import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')
    
    try:
        # Get a list of all S3 buckets
        response = s3.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        # Return the list of bucket names
        return {
            'statusCode': 200,
            'body': bucket_names
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error listing S3 buckets. Reason: {str(e)}'
        }