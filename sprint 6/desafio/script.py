import boto3
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('keys.env')

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'data-lake-Jonas'
RAW_ZONE = 'RAW/Local/CSV'

arquivos_locais = {
    'Movies': r'C:\Users\Jonas Gabriel\repo novo git\sprint 6\desafio\movies.csv',
    'Series': r'C:\Users\Jonas Gabriel\repo novo git\sprint 6\desafio\series.csv'
}

def upload_S3(file_path, data_type):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    s3 = session.resource('s3')

    today = datetime.today().strftime('%Y/%m/%d')


    s3_path = f'{RAW_ZONE}/{data_type}/{today}/{os.path.basename(file_path)}'

    try:
        s3.bucket(BUCKET_NAME).upload_file(file_path, s3_path)
        print(f'Upload de {file_path} concluído com sucesso para {s3_path}')
    except Exception as e:
        print(f'Erro no upload de {file_path}: {str(e)}')


for data_type, file_path in arquivos_locais.items():
    upload_S3(file_path, data_type)


