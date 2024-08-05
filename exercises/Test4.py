import sys
from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ButtonPressCounter")
        self.setGeometry(100, 100, 280, 80)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.counter = 0
        self.label = QLabel(f"Pressed time: {self.counter}  ", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Press me!!", self)
        layout.addWidget(self.button)

        # self.button.clicked.connect(self.count_button_press)
        self.button.clicked.connect(self.count_button_press)
    def count_button_press(self):
         if self.button.clicked.connect:
             self.counter += 1







def main():
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
