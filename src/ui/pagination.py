"""
test
"""
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt


class PaginationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.page_number: int = 0
        layout: QHBoxLayout = QHBoxLayout()
        self.prev_btn: QPushButton = QPushButton('<- Prev page')
        self.prev_btn.setEnabled(False)
        self.next_btn: QPushButton = QPushButton('Next page ->')
        self.next_btn.setEnabled(False)
        self.page_number_label: QLabel = QLabel(str(self.page_number))
        layout.addWidget(self.prev_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.page_number_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.next_btn, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(layout)

    def next_page(self):
        self.page_number += 1
        self.prev_btn.setEnabled(True)
        self.page_number_label.setText(str(self.page_number))

    def prev_page(self):
        if 0 < self.page_number:
            self.page_number -= 1
            if 0 == self.page_number:
                self.prev_btn.setEnabled(False)
            self.page_number_label.setText(str(self.page_number))

    def enable(self):
        self.next_btn.setEnabled(True)
        if 0 < self.page_number:
            self.prev_btn.setEnabled(True)
        else:
            self.prev_btn.setEnabled(False)

    def disable(self):
        self.next_btn.setEnabled(False)
        self.prev_btn.setEnabled(False)
