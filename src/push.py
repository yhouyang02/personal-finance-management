import boto3
import os
from botocore.exceptions import ClientError
import logging

def upload_image_to_s3(file_path, bucket_name, s3_key=None):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # If s3_key is not provided, use the original filename
    if s3_key is None:
        s3_key = os.path.basename(file_path)
    
    # Initialize S3 client
    try:
        s3_client = boto3.client('s3')
        
        # Check if file exists
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return False
            
        # Get file size
        file_size = os.path.getsize(file_path)
        logger.info(f"Uploading file: {file_path} ({file_size} bytes)")
        
        # Upload file
        with open(file_path, 'rb') as file_data:
            s3_client.upload_fileobj(
                file_data,
                bucket_name,
                s3_key,
                ExtraArgs={
                    'ContentType': 'image/jpg' 
                }
            )
            
        logger.info(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}")
        return True
        
    except ClientError as e:
        logger.error(f"AWS Error: {e}")
        return False
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return False

def upload_file_to_s3(file_path, bucket_name, s3_key=None):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # If s3_key is not provided, use the original filename
    if s3_key is None:
        s3_key = os.path.basename(file_path)
    
    # Initialize S3 client
    try:
        s3_client = boto3.client('s3')
        
        # Check if file exists
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return False
            
        # Get file size
        file_size = os.path.getsize(file_path)
        logger.info(f"Uploading file: {file_path} ({file_size} bytes)")
        
        # Upload file
        with open(file_path, 'rb') as file_data:
            s3_client.upload_fileobj(
                file_data,
                bucket_name,
                s3_key,
                ExtraArgs={
                    'ContentType': 'text/txt' 
                }
            )
            
        logger.info(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}")
        return True
        
    except ClientError as e:
        logger.error(f"AWS Error: {e}")
        return False
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return False

if __name__ == "__main__":
    bucket_name = "chiabucket-3"
    
    success = upload_image_to_s3(
        file_path="./temp/figure_barchart.jpg",
        bucket_name=bucket_name,
        s3_key="output/images/figure_barchart.jpg" 
    ) and upload_image_to_s3(
        file_path="./temp/figure_linechart.jpg",
        bucket_name=bucket_name,
        s3_key="output/images/figure_linechart.jpg" 
    ) and upload_file_to_s3(
        file_path="./temp/prediction.txt",
        bucket_name=bucket_name,
        s3_key="output/prediction.txt" 
    )
    
    if success:
        print("Upload completed successfully")
    else:
        print("Upload failed")