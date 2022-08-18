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
        self.setup_table()

    def setup_table(self):
        # layout = QGridLayout()
        # layout.addWidget(LabelCellWidget("Location"), 0, 0, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 1"), 0, 1, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 2"), 0, 2, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 3"), 0, 3, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 4"), 0, 4, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 5"), 0, 5, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 6"), 0, 6, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 7"), 0, 7, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(LabelCellWidget("Day 8"), 0, 8, Qt.AlignmentFlag.AlignTop)

        # self.add_button = QPushButton("+")
        # layout.addWidget(self.add_button, 1, 0, Qt.AlignmentFlag.AlignTop)

        # self.table = QWidget()
        # self.table.setLayout(layout)
        # self.setCentralWidget(self.table)

        self.table = QTableWidget(0, 9)
        self.table.setHorizontalHeaderLabels(["Location"] + [f"Day {i}" for i in range(1,9)])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()