"""
test
"""
from PyQt6.QtWidgets import QDialog, QListWidget, QHBoxLayout


class SearchResult(QDialog):
    """
    test
    """
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.search_list = QListWidget()
        layout.addWidget(self.search_list)
        self.setLayout(layout)
