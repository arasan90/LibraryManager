from PyQt6.QtWidgets import QPushButton

class LateralMenuButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.setCheckable(True)