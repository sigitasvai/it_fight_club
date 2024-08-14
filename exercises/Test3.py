import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QRect


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.parking_lot_pixmap = QPixmap(r"C:\Users\PC\Downloads\585_images\parking_lot.png")
        self.parked_car = QPixmap(r"C:\Users\PC\Downloads\585_images\parked_car.png")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())