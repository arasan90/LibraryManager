"""
test
"""
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from qt_material import apply_stylesheet


app = QApplication([])
window = MainWindow()
apply_stylesheet(app, theme='dark_amber.xml')
window.show()

app.exec()
