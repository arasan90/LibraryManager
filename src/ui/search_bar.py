"""
test
"""
from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit, QLabel
from PyQt6.QtCore import Qt


class SearchBar(QWidget):
    """
    test
    """
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.search_label = QLabel("Search bar")
        self.search_field = QLineEdit()
        self.search_button = QPushButton("Search")
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_field)
        layout.addSpacing(50)
        layout.addWidget(self.search_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(layout)
