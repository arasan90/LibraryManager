"""
test
"""
from PyQt6.QtWidgets import QDialog, QListWidget, QVBoxLayout, QListWidgetItem
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QThread
from ui.search_bar import SearchBar
from logic.info_retriever import InfoRetriever


class Worker(QObject):
    """
    Test
    """
    finished = pyqtSignal(list)

    def __init__(self, search_query):
        super().__init__()
        self.search_query = search_query

    def run(self):
        """Long-running task."""
        books_list = InfoRetriever.search(self.search_query)
        self.finished.emit(books_list)


class SearchResult(QDialog):
    """
    test
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.search_list = QListWidget()
        self.search_bar = SearchBar()
        self.search_bar.search_button.clicked.connect(self.perform_search)
        self.search_list.itemDoubleClicked.connect(self.open_details)
        layout.addWidget(self.search_bar, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.search_list)
        self.setLayout(layout)

    def perform_search(self, _is_checked):
        self.search_list.clear()
        self.thread = QThread()
        self.worker = Worker(self.search_bar.search_field.text())
        self.search_bar.search_button.setText("Searching...")
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.search_bar.search_button.setEnabled(False)
        self.worker.finished.connect(self.check_results)

    def check_results(self, books_list):
        self.books_list = books_list
        self.search_bar.search_button.setEnabled(True)
        self.search_bar.search_button.setText("Add new item")
        for book in books_list:
            authors = []
            try:
                for author in book["volumeInfo"]["authors"]:
                    authors.append(author)
            except Exception:
                authors.append("Unknown")
            finally:
                self.search_list.addItem(QListWidgetItem(f'{book["volumeInfo"]["title"]} {authors}'))
        self.thread.quit()
        self.worker.deleteLater()

    def open_details(self, item: QListWidgetItem):
        table_index = self.search_list.row(item)
        print(self.books_list[table_index])
