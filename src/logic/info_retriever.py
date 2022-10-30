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

    @staticmethod
    def get_summary(book_query: str):
        summary: str = ""
        try:
            response: requests.Response = requests.get(book_query)
            summary: bytes = json.loads(response.content)["volumeInfo"]["description"]
        except Exception:
            summary = ""
        return summary

    @staticmethod
    def get_thumbnail(resource_link: str):
        pic: bytes = ""
        try:
            response: requests.Response = requests.get(resource_link)
            pic = response.content
        except Exception:
            pic = ""
        return pic
