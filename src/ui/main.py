from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLineEdit, QLabel, QWidget, QDialog
from qt_material import apply_stylesheet
from lateral_menu import LateralMenu

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        lateral_menu = LateralMenu()
        button = QPushButton("Press Me!")
        button.clicked.connect(self.test)
        lineEdit = QLineEdit()
        lineEdit.setPlaceholderText("Test placeholder")
        lineEdit.setStyleSheet("color: white;")
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(lateral_menu)
        layout.addWidget(QLabel("Test label"))
        layout.addWidget(lineEdit)
        layout.addWidget(button)
        layout.addStretch()
        widget.setLayout(layout)
        menubar = self.menuBar()
        menubar.addMenu("File")
        self.dialog = QDialog()
        self.dialog.setModal(True)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        self.setMenuWidget(menubar)

    def test(self, checked):
        self.dialog.show()

app = QApplication([])
window = MainWindow()
apply_stylesheet(app, theme='dark_amber.xml')
window.show()

app.exec()
