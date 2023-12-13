import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget, QPushButton, QHBoxLayout
from solving import FactorialCalculatorApp
from devinisi import FactorialDefinitionApp

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Determine Factorial Number")
        layout = QStackedLayout()

        factorial = FactorialCalculatorApp()
        definisi = FactorialDefinitionApp()

        self.setStyleSheet("background-color:white")

        layout.addWidget(definisi)  # Index 0
        layout.addWidget(factorial)  # Index 1

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        button1 = QPushButton("Pengertian")
        button2 = QPushButton("Hitung Faktorial")

        button1.clicked.connect(lambda: layout.setCurrentIndex(0))
        button2.clicked.connect(lambda: layout.setCurrentIndex(1))

        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)
        buttons_widget.setLayout(buttons_layout)
        self.setMenuWidget(buttons_widget)
        self.setFixedSize(300, 500)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
