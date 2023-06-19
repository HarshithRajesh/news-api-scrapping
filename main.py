import os 
from dotenv import load_dotenv
import requests

load_dotenv()
API = os.getenv('API_KEY')

def get_news(topic):
    global API
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={API}'
    response = requests.get(url)
    content = response.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE : \n{article['title']}\nDESCRIPTION : \n{article['description']}")
    return results

print(get_news('stock'))