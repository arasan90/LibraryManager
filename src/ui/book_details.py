"""
test
"""
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLabel, QLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from logic.info_retriever import InfoRetriever


class BookDetails(QDialog):
    def __init__(self, pic_url: str, title: str, authors: list[str], summary: str):
        super().__init__()
        self.image_raw = InfoRetriever.get_thumbnail(pic_url)
        self.title = QLabel(f'Title: {title}')
        self.authors = QLabel(f'Authors: {authors}')
        self.summary = QLabel(f'Summary: {summary}')
        self.summary.setWordWrap(True)
        self.main_layout = QHBoxLayout()
        self.sub_layout = QVBoxLayout()
        self.add_button = QPushButton("Add")
        self.qpixmap = QPixmap()
        self.pic = QLabel()
        self.qpixmap.loadFromData(self.image_raw)
        self.pic.setPixmap(self.qpixmap)
        self.main_layout.addWidget(self.pic)
        self.sub_layout.addWidget(self.title)
        self.sub_layout.addWidget(self.authors)
        self.sub_layout.addWidget(self.summary)
        self.sub_layout.addWidget(self.add_button)
        self.main_layout.addLayout(self.sub_layout)
        self.sub_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.add_button.clicked.connect(self.add_book_to_library)
        self.setLayout(self.main_layout)

    def add_book_to_library(self):
        print("Saved")
