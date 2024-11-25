import boto3
import os

def download_from_s3(bucket_name, s3_file_key, local_file_name):
    """
    Download a file from S3 to the current directory in EC2
    
    Parameters:
    bucket_name (str): Name of the S3 bucket
    s3_file_key (str): Path to the file in S3 bucket (e.g., 'folder/file.csv')
    local_file_name (str): Name to save the file as in current directory
    """
    try:
        # Create an S3 client
        # No need to specify credentials as EC2 will use IAM role
        s3_client = boto3.client('s3')
        
        # Get the current working directory
        current_dir = os.getcwd()
        
        # Create the full local path
        local_file_path = os.path.join(current_dir, local_file_name)
        
        # Download the file
        s3_client.download_file(bucket_name, s3_file_key, local_file_path)
        print(f"Successfully downloaded {s3_file_key} to {local_file_path}")
        
    except Exception as e:
        print(f"Error downloading file: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace these values with your actual S3 bucket and file details
    BUCKET_NAME = "user-expenditure-data"
    S3_FILE_KEY = "./user_1_2022_241122024100"
    LOCAL_FILE_NAME = ".data/user/user_1_2022_241122024100"
    
    download_from_s3(BUCKET_NAME, S3_FILE_KEY, LOCAL_FILE_NAME)