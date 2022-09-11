from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QPushButton, QDialog
from PyQt6.QtCore import Qt, QObject, QThread, pyqtSignal
from ui.lateral_menu import LateralMenu
from ui.search_bar import SearchBar
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
        self.thread = QThread()
        self.worker = Worker()
        self.dialog = QDialog()
        self.dialog.setModal(True)
        self.new_item_btn.setText("Searching...")
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.new_item_btn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.new_item_btn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.dialog.show()
        )
        self.thread.started.connect(
            lambda: self.new_item_btn.setText("Add new item")
        )
