import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from src.location import LocationWeather

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RainTable")
        self.setWindowIcon(QIcon("icons/water.png"))
        self.resize(QSize(1920, 1080))

        # Setup
        self.row_LW = dict()
        self.setup_widgets()

    def setup_widgets(self):
        # Create table widget and set headers
        self.table = QTableWidget(1, 9)
        self.last_row = 0
        self.table.setHorizontalHeaderLabels(["Location"] + [f"Day {i}" for i in range(1,9)])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)

        # Disable editing of day columns
        for c in range(1, 9):
            item = QTableWidgetItem()
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(0, c, item)
        self.table.cellChanged.connect(self.addLocation)

        # Set up layout
        self.main = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.main.setLayout(layout)
        self.setCentralWidget(self.main)

    def addLocation(self, row, col):
        if col == 0:
            address = self.table.item(row, col).text()

            # If last row is edited, add another row
            if row == self.last_row:
                self.table.insertRow(row+1)
                self.last_row += 1
                
                for c in range(1, 9):
                    item = QTableWidgetItem()
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                    self.table.setItem(self.last_row, c, item)

            # Create LocationWeather
            self.row_LW[row] = LocationWeather(address)
            for c in range(1, 9):
                item = self.table.item(row, c)
                weather = self.row_LW[row].get_weather(c-1)
                temp = self.row_LW[row].get_temp(c-1)
                pop = self.row_LW[row].get_POP(c-1)
                item.setText(f"{pop * 100}% " + f"{weather[0]['description']}".capitalize())
                item.setToolTip(f"Min: {temp['min']} F\nMax: {temp['max']} F")

                code = weather[0]['id']
                if code in range(200, 233):
                    item.setIcon(QIcon("icons/thunderstorm.png"))
                elif code in range(300, 322):
                    item.setIcon(QIcon("icons/drizzle.png"))
                elif code in range(500, 532):
                    item.setIcon(QIcon("icons/rain.png"))
                elif code in range(600, 623):
                    item.setIcon(QIcon("icons/snow.png"))
                elif code in range(700, 782):
                    item.setIcon(QIcon("icons/fog.png"))
                elif code == 800:
                    item.setIcon(QIcon("icons/sunny.png"))
                elif code == 801 or code == 802:
                    item.setIcon(QIcon("icons/cloudy.png"))
                elif code == 803 or code == 804:
                    item.setIcon(QIcon("icons/overcast.png"))


app = QApplication([])

window = MainWindow()
window.show()

app.exec()