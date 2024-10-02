import boto3
import pandas as pd
import os
from dotenv import load_dotenv

result = load_dotenv(dotenv_path='keys.env')
print(f"Arquivo .env carregado? {result}")

