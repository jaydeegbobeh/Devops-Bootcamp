import logging
import boto3
from botocore.exceptions import ClientError
import os

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

def upload_to_bucket(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

def empty_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()



print("S3 bucket manager")
print("Select option:")
print("1. Create bucket")
print("2. Upload object to bucket")
print("3. Download object from bucket")
print("4. Delete all objects in bucket")
print("5. Delete bucket")
print("Enter exit to quit")
while True:
    choice = input("Enter choice(1-5): ")

    if choice == '1':
        bucket_name = input("Enter bucket name: ")
        region = input("Enter region: ")
        create_bucket(bucket_name, region)
    if choice == '2':
        bucket_name = input("Enter bucket name: ")
        file_name = input("Enter file name: ")
        object_name = file_name
        upload_to_bucket(file_name, bucket_name, object_name)
    if choice == '3':
        BUCKET_NAME = input("Enter bucket name: ")
        BUCKET_FILE_NAME = input("Enter file that you want to download: ")
        LOCAL_FILE_NAME = input ("Save file as: ")
        download_file()
    if choice == '4':
        bucket_name = input("Enter bucket name: ")
        empty_bucket(bucket_name)
    if choice == '5':
        bucket_name = input("Enter bucket: ")
        delete_bucket(bucket_name)

# bucket_name = "jaydee-bucket"
# region = "eu-west-1"
# BUCKET_FILE_NAME = "test.md"
# LOCAL_FILE_NAME = "test_download.md"
# download_file()
# create_bucket(bucket_name, region)
empty_bucket(bucket_name)
