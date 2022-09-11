from turtle import width
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QSizePolicy
from PyQt6.QtCore import *
from qt_material import apply_stylesheet
from lateral_menu import LateralMenu
from search_bar import SearchBar

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = QWidget()
        lateral_menu = LateralMenu()
        search_bar = SearchBar()
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        root_layout = QHBoxLayout()
        sub_layout = QVBoxLayout()
        sub_layout.addWidget(search_bar)
        sub_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        root_layout.addWidget(lateral_menu)
        root_layout.addWidget(v_line)
        root_layout.addLayout(sub_layout)
        root_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        widget.setLayout(root_layout)
        menubar = self.menuBar()
        menubar.addMenu("File")

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        self.setMenuWidget(menubar)

app = QApplication([])
window = MainWindow()
apply_stylesheet(app, theme='dark_amber.xml')
window.show()

app.exec()
