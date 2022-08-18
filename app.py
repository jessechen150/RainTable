import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from src.location import LocationWeather
from src.cell import LabelCellWidget, WeatherCellWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RainTable")
        self.setWindowIcon(QIcon("icons/water.png"))
        self.resize(QSize(1000, 500))

        # Setup widgets
        self.setup_widget()

    def setup_widget(self):
        self.table = QTableWidget(1, 9)
        self.table.setHorizontalHeaderLabels(["Location"] + [f"Day {i}" for i in range(1,9)])
        self.table.verticalHeader().setVisible(False)

        item = QTableWidgetItem()
        # Create weather cell that inherits QTableWidgetItem?
        item.setText("Hello")
        self.table.setItem(0, 0, item)

        self.main = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.main.setLayout(layout)
        self.setCentralWidget(self.main)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()