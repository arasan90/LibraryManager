from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QPushButton
# Add QThread in PyQt6.QtCore
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from ui.lateral_menu import LateralMenu
from ui.search_bar import SearchBar
from ui.seach_result import SearchResult
from logic.info_retriever import InfoRetriever


class Worker(QObject):
    """
    Test
    """
    finished = pyqtSignal()

    def run(self):
        """Long-running task."""
        InfoRetriever.search()
        self.finished.emit()


class MainWindow(QMainWindow):
    """
    test
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = QWidget()
        lateral_menu = LateralMenu()
        search_bar = SearchBar()
        self.new_item_btn = QPushButton("Add new item")
        self.new_item_btn.clicked.connect(self.add_new_item)
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        root_layout = QHBoxLayout()
        sub_layout = QVBoxLayout()
        sub_layout.addWidget(search_bar, alignment=Qt.AlignmentFlag.AlignTop)
        sub_layout.addWidget(self.new_item_btn, alignment=Qt.AlignmentFlag.AlignBottom)
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

    def add_new_item(self):
        self.dialog = SearchResult()
        self.dialog.setModal(True)
        self.dialog.show()
