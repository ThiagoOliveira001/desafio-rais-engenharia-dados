from dotenv import load_dotenv
import boto3
import os

load_dotenv()

dirname = os.path.dirname(__file__)

ACCESS_ID=os.getenv('ACCESS_ID')
ACCESS_KEY=os.getenv('ACCESS_KEY')
DATA_DIR=os.path.join(dirname, os.getenv('DATA_DIR', 'dados_rais'))
BUCKET=os.getenv('BUCKET')

def get_files_to_upload(dir):
    files_to_upload = list()
    files = os.listdir(dir)

    for file in files:
        path_file = os.path.join(dir, file)
        is_dir = os.path.isdir(path_file)
        if (is_dir):
            files_to_upload.extend(get_files_to_upload(path_file))
            continue
        files_to_upload.append(path_file)
    return files_to_upload

files_to_upload = get_files_to_upload(DATA_DIR)
s3_client = boto3.client('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)

files_qtd = len(files_to_upload)
for index, file_path in enumerate(files_to_upload):
    file = file_path.split(sep="\\").pop(-1)
    s3_client.upload_file(file_path, BUCKET, f'raw-data/rais/year=2020/{file}')
    print(f'Uploaded {file} {index + 1} of {files_qtd}')

print(f'Upload {files_qtd}')