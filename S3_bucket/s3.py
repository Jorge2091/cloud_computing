from botocore.exceptions import ClientError
import boto3



def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3 = boto3.client('s3')
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3 = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError:
        
        return Print("error connecting, please check configuration or name")
    return print(f"Successful created bucket with name {bucket_name}")

import os


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError:
        
        return print("cant connect or upload")
    return print("uploaded")

def download(bucket, object_name, new_name):
    s3 = boto3.client
    s3.download_file(bucket, object_name, new_name)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError:
        
        return print("cant connect or download")
    return print("downloaded")

create_bucket("eng130-jorge", "eu-west-1")