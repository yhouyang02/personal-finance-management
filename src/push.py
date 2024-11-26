import boto3
import os
from botocore.exceptions import ClientError
import logging

def upload_image_to_s3(file_path, bucket_name, s3_key=None):
    """
    Upload an image from EC2 to S3 bucket
    
    Parameters:
    file_path (str): Local path to the image file on EC2
    bucket_name (str): Name of the S3 bucket
    s3_key (str): The desired name/path of the file in S3 (optional)
    
    Returns:
    bool: True if file was uploaded, else False
    """
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
                    'ContentType': 'image/jpeg' 
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
    image_path = "./temp/figure.jpg"
    bucket_name = "chiabucket-3"
    
    success = upload_image_to_s3(
        file_path=image_path,
        bucket_name=bucket_name,
        s3_key="images/figure_barchart.jpg" 
    ) and upload_image_to_s3(
        file_path=image_path,
        bucket_name=bucket_name,
        s3_key="images/figure_linechart.jpg" 
    )
    
    if success:
        print("Upload completed successfully")
    else:
        print("Upload failed")