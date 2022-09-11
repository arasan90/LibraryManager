"""
test
"""
from lateral_menu_button import LateralMenuButton
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class LateralMenu(QWidget):
    """
    test
    """
    def __init__(self):
        super().__init__()
        layout: QVBoxLayout = QVBoxLayout()
        self.books_button: QPushButton = LateralMenuButton("Books")
        self.books_button.setChecked(True)
        self.movies_button: QPushButton = LateralMenuButton("Movies")
        self.games_button: QPushButton = LateralMenuButton("Games")
        self.books_button.clicked.connect(self.manage_books_button_click)
        self.movies_button.clicked.connect(self.manage_movies_button_click)
        self.games_button.clicked.connect(self.manage_games_button_click)
        layout.addWidget(self.books_button)
        layout.addWidget(self.movies_button)
        layout.addWidget(self.games_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    def manage_books_button_click(self, _is_checked):
        """
        test
        """
        self.books_button.setChecked(True)
        self.movies_button.setChecked(False)
        self.games_button.setChecked(False)

    def manage_movies_button_click(self, _is_checked):
        """
        test
        """
        self.books_button.setChecked(False)
        self.movies_button.setChecked(True)
        self.games_button.setChecked(False)

    def manage_games_button_click(self, _is_checked):
        """
        test
        """
        self.books_button.setChecked(False)
        self.movies_button.setChecked(False)
        self.games_button.setChecked(True)
