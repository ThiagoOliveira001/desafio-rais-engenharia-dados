from dotenv import load_dotenv
import boto3
import os

load_dotenv()

dirname = os.path.dirname(__file__)

ACCESS_ID=os.getenv('ACCESS_ID')
ACCESS_KEY=os.getenv('ACCESS_KEY')
DATA_DIR=os.path.join(dirname, os.getenv('DATA_DIR', 'dados_rais'))


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
