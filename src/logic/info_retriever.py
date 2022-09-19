import requests
import json


class InfoRetriever():
    def __init__(self) -> None:
        pass

    @staticmethod
    def search(book_query: str, start_ix: int = 0):
        volumes = []
        response: requests.Response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book_query}&maxResults=40&orderBy=relevance&startIndex={start_ix}")
        raw_data: bytes = response.content
        data = json.loads(raw_data)
        try:
            volumes = data["items"]
        except Exception:
            volumes = []
        return response.status_code, volumes
