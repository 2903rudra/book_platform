import urllib.request
import urllib.parse
import json


GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes?q=search+terms'

def fetch_books(query):
    query_params = urllib.parse.urlencode({'q': query})
    url = f"{GOOGLE_BOOKS_API_URL}?{query_params}"
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                data = response.read()
                return json.loads(data)
            else:
                return {'error': 'Failed to fetch data from Google Books API'}
    except Exception as e:
        return {'error': str(e)}