"""
test
"""
from PyQt6.QtWidgets import QDialog, QListWidget, QVBoxLayout, QListWidgetItem, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QThread
from ui.search_bar import SearchBar
from ui.pagination import PaginationWidget
from ui.book_details import BookDetails
from logic.info_retriever import InfoRetriever


class Worker(QObject):
    """
    Test
    """
    finished = pyqtSignal(int, list)

    def __init__(self, search_query, page=0):
        super().__init__()
        self.page = page
        self.search_query = search_query

    def run(self):
        """Long-running task."""
        code, books_list = InfoRetriever.search(self.search_query, (self.page * 40))
        self.finished.emit(code, books_list)


class SearchResult(QDialog):
    """
    test
    """
    def __init__(self):
        super().__init__()
        self.page = 0
        self.save_page_number: bool = False
        layout = QVBoxLayout()
        self.search_list = QListWidget()
        self.search_bar = SearchBar()
        self.pagination_menu = PaginationWidget()
        self.pagination_menu.prev_btn.clicked.connect(self.prev_page_results)
        self.pagination_menu.next_btn.clicked.connect(self.next_page_results)
        self.search_bar.search_button.clicked.connect(self.perform_search)
        self.search_list.itemDoubleClicked.connect(self.open_details)
        layout.addWidget(self.search_bar, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.search_list)
        layout.addWidget(self.pagination_menu, alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(layout)

    def perform_search(self, _is_checked):
        query: str = self.search_bar.search_field.text()
        if not self.save_page_number:
            self.page = 0
            self.pagination_menu.reset()
        self.save_page_number = False
        self.search_list.clear()
        self.pagination_menu.disable()
        self.thread = QThread()
        self.worker = Worker(query, self.page)
        self.search_bar.search_button.setText("Searching...")
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.search_bar.search_button.setEnabled(False)
        self.worker.finished.connect(self.add_results)

    def prev_page_results(self, _is_checked):
        self.page -= 1
        self.pagination_menu.prev_page()
        self.save_page_number = True
        self.perform_search(False)

    def next_page_results(self, _is_checked):
        self.page += 1
        self.pagination_menu.next_page()
        self.save_page_number = True
        self.perform_search(False)

    def add_results(self, code, books_list):
        error_box = QMessageBox()
        error_box.setText("Error retrieving data")
        if (200 == code):
            self.books_list = books_list
            for book in books_list:
                authors = []
                try:
                    for author in book["volumeInfo"]["authors"]:
                        authors.append(author)
                except Exception:
                    authors.append("Unknown")
                finally:
                    self.search_list.addItem(QListWidgetItem(f'{book["volumeInfo"]["title"]} {authors}'))
            self.pagination_menu.enable()
        else:
            error_box.exec()
        self.search_bar.search_button.setEnabled(True)
        self.search_bar.search_button.setText("Add new item")
        self.thread.quit()
        self.worker.deleteLater()

    def open_details(self, item: QListWidgetItem):
        table_index = self.search_list.row(item)
        book = self.books_list[table_index]
        more_info_link = book["selfLink"]
        summary = InfoRetriever.get_summary(more_info_link)
        book_title = book["volumeInfo"]["title"]
        book_authors = book["volumeInfo"]["authors"]
        book_pic = book["volumeInfo"]["imageLinks"]["thumbnail"]
        self.book_details = BookDetails(book_pic, book_title, book_authors, summary)
        self.book_details.setModal(True)
        self.book_details.show()
