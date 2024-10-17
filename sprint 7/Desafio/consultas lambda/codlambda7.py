import json
import requests
import boto3
import os

def lambda_handler(event, context):
    api_key = os.environ['TMDB_API_KEY']
    
    movie_title = "Como Eu Era Antes de Você"
    movie_data = get_movie_data(api_key, movie_title)

    store_movie_in_s3(movie_data)

    return {
        'statusCode': 200,
        'body': json.dumps(movie_data)
    }

def get_movie_data(api_key, movie_title):
    base_url = "https://api.themoviedb.org/3"
    
    search_url = f"{base_url}/search/movie?api_key={api_key}&language=pt-BR&query={movie_title}"
    search_response = requests.get(search_url)

    if search_response.status_code == 200:
        search_results = search_response.json()
        
        if search_results['results']:
            movie_id = search_results['results'][0]['id']  
            movie_details_url = f"{base_url}/movie/{movie_id}?api_key={api_key}&language=pt-BR&append_to_response=credits"
            movie_details_response = requests.get(movie_details_url)

            if movie_details_response.status_code == 200:
                movie_data = movie_details_response.json()
                return {
                    'id': movie_data['id'],
                    'title': movie_data['title'],
                    'release_date': movie_data['release_date'],
                    'runtime': movie_data['runtime'],
                    'vote_average': movie_data['vote_average'],
                    'popularity': movie_data['popularity'],
                    'cast': [actor['name'] for actor in movie_data.get('credits', {}).get('cast', [])[:5]]  
                }
            else:
                return {'error': 'Não foi possível obter os detalhes do filme.'}
        else:
            return {'error': 'Filme não encontrado.'}
    else:
        return {'error': 'Erro na busca do filme.'}

def store_movie_in_s3(movie_data):
    s3 = boto3.client('s3')
    bucket_name = 'data-lake-jonas'
    path_prefix = 'Raw/TMDB/JSON/2024/10/17/como_eu_era_antes_de_voce.json'
    
    file_name = f"{path_prefix}{movie_data['id']}.json"  
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(movie_data),
        ContentType='application/json'
    )

