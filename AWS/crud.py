import logging
import boto3
from bootcore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    if region is None:
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3 = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)


def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)

def upload_to_bucket(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3 = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_from_bucket(bucket_name, file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, object_name)

bucket_name = "devops-jaydee-bucket-test"
region = "eu-west-1"
create_bucket(bucket_name, region)
