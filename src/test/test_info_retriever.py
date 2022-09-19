import unittest
from unittest.mock import MagicMock, patch
from logic.info_retriever import InfoRetriever


class TestInfoRetrieval(unittest.TestCase):

    @patch('logic.info_retriever.requests')
    def test_retrieval_ok(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = """{
        "kind": "books#volumes",
        "totalItems": 1745,
        "items": [
        {
            "kind": "books#volume",
            "id": "_LaRzQEACAAJ",
            "etag": "2/WATo1C7jc",
            "selfLink": "https://www.googleapis.com/books/v1/volumes/_LaRzQEACAAJ",
            "volumeInfo": {
                "title": "Cronache marziane",
                "authors": [
                    "Ray Bradbury"
                ],
                "publishedDate": "2020",
                "industryIdentifiers": [
                    {
                        "type": "ISBN_10",
                        "identifier": "8804724870"
                    },
                    {
                        "type": "ISBN_13",
                        "identifier": "9788804724872"
                    }
                ],
                "readingModes": {
                    "text": "false",
                    "image": "false"
                },
                "pageCount": 276,
                "printType": "BOOK",
                "categories": [
                    "Fiction"
                ],
                "maturityRating": "NOT_MATURE",
                "allowAnonLogging": "false",
                "contentVersion": "preview-1.0.0",
                "panelizationSummary": {
                    "containsEpubBubbles": "false",
                    "containsImageBubbles": "false"
                },
                "imageLinks": {
                    "smallThumbnail": "http://books.google.com/books/content?id=_LaRzQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=_LaRzQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                },
                "language": "it",
                "previewLink": "http://books.google.it/books?id=_LaRzQEACAAJ&dq=Cronache&hl=&cd=1&source=gbs_api",
                "infoLink": "http://books.google.it/books?id=_LaRzQEACAAJ&dq=Cronache&hl=&source=gbs_api",
                "canonicalVolumeLink": "https://books.google.com/books/about/Cronache_marziane.html?hl=&id=_LaRzQEACAAJ"
            },
            "saleInfo": {
                "country": "IT",
                "saleability": "NOT_FOR_SALE",
                "isEbook": "false"
            },
            "accessInfo": {
                "country": "IT",
                "viewability": "NO_PAGES",
                "embeddable": "false",
                "publicDomain": "false",
                "textToSpeechPermission": "ALLOWED",
                "epub": {
                    "isAvailable": "false"
                },
                "pdf": {
                    "isAvailable": "false"
                },
                "webReaderLink": "http://play.google.com/books/reader?id=_LaRzQEACAAJ&hl=&printsec=frontcover&source=gbs_api",
                "accessViewStatus": "NONE",
                "quoteSharingAllowed": "false"
            }
        },
        {
            "kind": "books#volume",
            "id": "bRDVmQEACAAJ",
            "etag": "c4zb/Nmbf5s",
            "selfLink": "https://www.googleapis.com/books/v1/volumes/bRDVmQEACAAJ",
            "volumeInfo": {
                "title": "Cronache della famiglia Wapshot",
                "authors": [
                    "John Cheever"
                ],
                "publishedDate": "2013",
                "industryIdentifiers": [
                    {
                        "type": "ISBN_10",
                        "identifier": "8807881837"
                    },
                    {
                        "type": "ISBN_13",
                        "identifier": "9788807881831"
                    }
                ],
                "readingModes": {
                    "text": "false",
                    "image": "false"
                },
                "pageCount": 378,
                "printType": "BOOK",
                "categories": [
                    "Fiction"
                ],
                "maturityRating": "NOT_MATURE",
                "allowAnonLogging": "false",
                "contentVersion": "preview-1.0.0",
                "imageLinks": {
                    "smallThumbnail": "http://books.google.com/books/content?id=bRDVmQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                    "thumbnail": "http://books.google.com/books/content?id=bRDVmQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                },
                "language": "it",
                "previewLink": "http://books.google.it/books?id=bRDVmQEACAAJ&dq=Cronache&hl=&cd=2&source=gbs_api",
                "infoLink": "http://books.google.it/books?id=bRDVmQEACAAJ&dq=Cronache&hl=&source=gbs_api",
                "canonicalVolumeLink": "https://books.google.com/books/about/Cronache_della_famiglia_Wapshot.html?hl=&id=bRDVmQEACAAJ"
            },
            "saleInfo": {
                "country": "IT",
                "saleability": "NOT_FOR_SALE",
                "isEbook": "false"
            },
            "accessInfo": {
                "country": "IT",
                "viewability": "NO_PAGES",
                "embeddable": "false",
                "publicDomain": "false",
                "textToSpeechPermission": "ALLOWED",
                "epub": {
                    "isAvailable": "false"
                },
                "pdf": {
                    "isAvailable": "false"
                },
                "webReaderLink": "http://play.google.com/books/reader?id=bRDVmQEACAAJ&hl=&printsec=frontcover&source=gbs_api",
                "accessViewStatus": "NONE",
                "quoteSharingAllowed": "false"
            }
        }
    ]
  }"""
        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response
        status_code, books = InfoRetriever.search("test")
        self.assertEqual(200, status_code)
        self.assertIsNotNone(books)
