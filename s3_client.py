import boto3
from botocore.exceptions import ClientError


class S3Client:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region_name='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
    
    def upload_file(self, file_path, bucket_name, object_name=None):
        if object_name is None:
            object_name = file_path.split('/')[-1]
        
        try:
            self.s3_client.upload_file(file_path, bucket_name, object_name)
            return f"s3://{bucket_name}/{object_name}"
        except ClientError as e:
            raise Exception(f"Failed to upload file: {str(e)}")
    
    def download_file(self, bucket_name, object_name, file_path):
        try:
            self.s3_client.download_file(bucket_name, object_name, file_path)
            return file_path
        except ClientError as e:
            raise Exception(f"Failed to download file: {str(e)}")
    
    def list_files(self, bucket_name, prefix=''):
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            return []
        except ClientError as e:
            raise Exception(f"Failed to list files: {str(e)}")
