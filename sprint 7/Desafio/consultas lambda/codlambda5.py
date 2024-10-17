import json
import requests
import boto3
import os

def lambda_handler(event, context):
    api_key = os.environ['TMDB_API_KEY']
    
    movie_data = get_movie_data(api_key, 11631)  
    
    # Armazenar os dados no S3
    store_movie_data_in_s3(movie_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(movie_data)
    }

def get_movie_data(api_key, movie_id):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    url = f"{base_url}?api_key={api_key}&language=pt-BR"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        return {
            'id': movie_data['id'],
            'title': movie_data['title'],
            'vote_average': movie_data['vote_average'],
            'popularity': movie_data['popularity']
        }
    else:
        return {}

def store_movie_data_in_s3(movie_data):
    s3 = boto3.client('s3')
    bucket_name = 'data-lake-jonas'
    file_name = 'Raw/TMDB/JSON/2024/10/17/mamma_mia.json'
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(movie_data),
        ContentType='application/json'
    )
