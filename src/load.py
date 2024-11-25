import boto3
import os

def download_from_s3(bucket_name, s3_file_key, local_file_name, aws_access_key, aws_secret_key, region='us-east-1'):
    """
    Download a file from S3 using AWS credentials
    
    Parameters:
    bucket_name (str): Name of the S3 bucket
    s3_file_key (str): Path to the file in S3 bucket (e.g., 'folder/file.csv')
    local_file_name (str): Name to save the file as in current directory
    aws_access_key (str): AWS access key ID
    aws_secret_key (str): AWS secret access key
    region (str): AWS region where the bucket is located
    """
    try:
        # Create an S3 client with explicit credentials
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )
        
        # Create the full local path
        local_file_path = os.path.join(os.getcwd(), local_file_name)
        
        # Download the file
        s3_client.download_file(bucket_name, s3_file_key, local_file_path)
        print(f"Successfully downloaded {s3_file_key} to {local_file_path}")

    except Exception as e:
        print(f"Error downloading file: {str(e)}")

if __name__ == "__main__":
    # Your AWS credentials
    AWS_ACCESS_KEY = 'ASIA45Y2R7YF2GD3DFUW'
    AWS_SECRET_KEY = 'rBfLa0Fu6lVbcg3bnt716qwhOtSc1kJJh2FURl/X'
    
    # Your S3 details
    BUCKET_NAME = "user-expenditure-data"
    S3_FILE_KEY = "user_1_2022_241122024100.csv"  # e.g., "folder/data.csv"
    LOCAL_FILE_NAME = "user_1_2022_241122024100.csv"
    REGION = "ca-central-1"  # Change to your bucket's region
    
    download_from_s3(
        bucket_name=BUCKET_NAME,
        s3_file_key=S3_FILE_KEY,
        local_file_name=LOCAL_FILE_NAME,
        aws_access_key=AWS_ACCESS_KEY,
        aws_secret_key=AWS_SECRET_KEY,
        region=REGION
    )