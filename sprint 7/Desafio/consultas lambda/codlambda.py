import json
import requests
import boto3
import os

def lambda_handler(event, context):
    api_key = os.environ['TMDB_API_KEY']
    
    movies = get_twilight_movies(api_key)
    
    store_movies_in_s3(movies)

    return {
        'statusCode': 200,
        'body': json.dumps(movies)
    }

def get_twilight_movies(api_key):
    base_url = "https://api.themoviedb.org/3"
    twilight_movies = []
    
    movie_ids = [8966, 50619, 50620, 24021] 

    for movie_id in movie_ids:
        url = f"{base_url}/movie/{movie_id}?api_key={api_key}&language=pt-BR&append_to_response=credits"
        response = requests.get(url)

        if response.status_code == 200:
            movie_data = response.json()
            cast = []
            if 'credits' in movie_data: 
                cast = [actor['name'] for actor in movie_data['credits'].get('cast', [])[:5]]  
            
            twilight_movies.append({
                'id': movie_data['id'],
                'title': movie_data['title'],
                'release_date': movie_data['release_date'],
                'runtime': movie_data['runtime'],
                'vote_average': movie_data['vote_average'],
                'popularity': movie_data['popularity'],
                'cast': cast
            })

    return twilight_movies

def store_movies_in_s3(movies):
    s3 = boto3.client('s3')
    bucket_name = 'data-lake-jonas'
    path_prefix = 'Raw/TMDB/JSON/2024/10/17/movies_'
    
    for i in range(0, len(movies), 100):
        batch = movies[i:i + 100]
        file_name = f"{path_prefix}{i // 100 + 1}.json"  
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(batch),
            ContentType='application/json'
        )
