import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtCore import Qt, QRect


class ParkingLotWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parking Lot")
        self.setGeometry(100, 100, 500, 300)

        self.parking_lot_pixmap = QPixmap(r"C:\Users\PC\Downloads\585_images\parking_lot.png")
        self.parked_car_pixmap = QPixmap(r"C:\Users\PC\Downloads\585_images\parked_car.png")

        self.parked_cars = []
        self.parking_slots = [(20, 50), (140, 50), (260, 50), (380, 50), (500, 50)]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.parking_lot_pixmap)

        for idx, car in enumerate(self.parked_cars):
            if car:
                x, y = self.parking_slots[idx]
                painter.drawPixmap(x, y, self.parked_car_pixmap)

    def add_car(self, plate_number):
        if len(self.parked_cars) < 5:
            self.parked_cars.append(plate_number)
            self.update()
            print(self.parked_cars)
        else:
            QMessageBox.warning(self, "Parking Full", "Parking lot is full.")

    def remove_car(self, plate_number):
        for number in self.parked_cars:
            if number == plate_number:
                self.parked_cars.remove(number)
                print(self.parked_cars)

            else:
                QMessageBox.warning(self, "Error", "Invalid plate number!")

◘
class ControlWindow(QWidget):
    def __init__(self, parking_lot_window):
        super().__init__()

        self.parking_lot_window = parking_lot_window

        self.setWindowTitle("Parking Control")
        self.setGeometry(650, 100, 300, 150)

        self.plate_enter_field = QLineEdit(self)
        self.plate_enter_field.setPlaceholderText("Enter Car Plate Number")

        self.plate_leave_field = QLineEdit(self)
        self.plate_leave_field.setPlaceholderText("Leave Car Plate Number")

        self.enter_button = QPushButton("Park Car", self)
        self.enter_button.clicked.connect(self.park_car)

        self.leave_button = QPushButton("Remove Car", self)
        self.leave_button.clicked.connect(self.remove_car)

        layout = QVBoxLayout()
        layout.addWidget(self.plate_enter_field)
        layout.addWidget(self.enter_button)
        layout.addWidget(self.plate_leave_field)
        layout.addWidget(self.leave_button)

        self.setLayout(layout)

    def park_car(self):
        plate_number = self.plate_enter_field.text().strip()
        if plate_number:
            self.parking_lot_window.add_car(plate_number)
            self.plate_enter_field.clear()

    def remove_car(self):
        plate_number = self.plate_leave_field.text().strip()
        if plate_number:
            self.parking_lot_window.remove_car(plate_number)
            self.plate_leave_field.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    parking_lot_window = ParkingLotWindow()
    control_window = ControlWindow(parking_lot_window)

    parking_lot_window.show()
    control_window.show()

    sys.exit(app.exec_())
