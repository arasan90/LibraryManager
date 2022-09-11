import requests
import json
from types import SimpleNamespace


def __init__():
    pass


class InfoRetriever():
    def __init__(self) -> None:
        pass

    @staticmethod
    def search():
        response: requests.Response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Licia Troisi")
        raw_data: bytes = response.content
        data = json.loads(raw_data)
        x = json.loads(raw_data, object_hook=lambda d: SimpleNamespace(**d))
        for book in data["items"]:
            print(book["volumeInfo"]["title"])
        for book in x.items:
            print(book.volumeInfo.title)
