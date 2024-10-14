import boto3
import logging
from botocore.exceptions import ClientError
from datetime import datetime
import os
from secrets import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, BUCKET_NAME

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Definindo a data atual para a estrutura do bucket
now = datetime.now()
DATA_ATUAL = now.strftime('%Y/%m/%d')

# Nomes dos arquivos CSV e chaves S3 correspondentes 
ARQUIVOS = ['/app/data/movies.csv', '/app/data/series.csv']
S3_KEYS = [f'Raw/Local/CSV/Movies/{DATA_ATUAL}/movies.csv',
           f'Raw/Local/CSV/Series/{DATA_ATUAL}/series.csv']

def bucket_exists(bucket_name):
    """Verifica se um bucket existe no S3."""
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token = AWS_SESSION_TOKEN)
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            logging.error(f'Bucket {bucket_name} não encontrado.')
        else:
            logging.error(f'Erro ao verificar o bucket: {e}')
        return False

def create_bucket(bucket_name, region=None):
    """Cria um bucket no S3 se ele não existir."""
    if bucket_exists(bucket_name):
        logging.info(f'O bucket "{bucket_name}" já existe.')
        return True
    
    try:
        if region is None:
            s3_client = boto3.client(
            's3', 
            aws_access_key_id=AWS_ACCESS_KEY, 
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token = AWS_SESSION_TOKEN)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client(
            's3', 
            aws_access_key_id=AWS_ACCESS_KEY, 
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token = AWS_SESSION_TOKEN,
            region_name=region)                  
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        logging.info(f'Bucket "{bucket_name}" criado com sucesso.')
    except ClientError as e:
        logging.error(f'Erro ao criar o bucket: {e}')
        return False

    return True

def upload_to_s3(arquivos, bucket_name, s3_keys):
    """Faz o upload dos arquivos CSV para o S3."""
    if not bucket_exists(bucket_name):
        logging.info(f'O bucket "{bucket_name}" não existe e será criado.')
        if not create_bucket(bucket_name):
            logging.error("Erro ao criar o bucket. Processo abortado.")
            return
    
    s3_client = boto3.client(
        's3', 
        aws_access_key_id=AWS_ACCESS_KEY, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token = AWS_SESSION_TOKEN)

    # Fazer o upload dos arquivos para o S3
    for arquivo, s3_key in zip(arquivos, s3_keys):
        try:
            s3_client.upload_file(arquivo, bucket_name, s3_key)
            logging.info(f'Upload do arquivo {arquivo} realizado com sucesso!')
        except ClientError as e:
            logging.error(f'Erro ao realizar o upload do arquivo {arquivo} para {s3_key}: {e}')      

if __name__ == '__main__':
    upload_to_s3(ARQUIVOS, BUCKET_NAME, S3_KEYS)