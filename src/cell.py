from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class LabelCellWidget(QLabel):
    def __init__(self, label):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#DE0000"))
        self.setPalette(palette)
        self.setText(label)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class WeatherCellWidget(QWidget):
    def __init__(self, lw: "LocationWeather"):
        super().__init__()
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#FFFFFF"))
        self.setPalette(palette)