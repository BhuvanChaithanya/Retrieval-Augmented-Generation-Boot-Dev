import json
from pathlib import Path 

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT/'data'
MOVIE_PATH = DATA_PATH/'movies.json'
STOPWORD_PATH = DATA_PATH/'stopwords.txt'
def load_movies() -> list[dict]:
    with open(MOVIE_PATH, "r") as f:
        data = json.load(f)
    return data['movies']

def load_stopwords() -> list[str]:
    with open(STOPWORD_PATH, "r") as f:
        data = f.read().splitlines()
    return data