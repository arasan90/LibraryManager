import requests
import json
# from types import SimpleNamespace


def __init__():
    pass


class InfoRetriever():
    def __init__(self) -> None:
        pass

    @staticmethod
    def search(book_query: str):
        response: requests.Response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book_query}&maxResults=40&orderBy=relevance")
        raw_data: bytes = response.content
        data = json.loads(raw_data)
        # x = json.loads(raw_data, object_hook=lambda d: SimpleNamespace(**d))
        return data["items"]
