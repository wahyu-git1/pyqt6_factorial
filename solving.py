from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class FactorialCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Masukkan Bilangan bulat:')
        self.input_field = QLineEdit(self)
        self.result_label = QLabel('Hasil:')
        self.steps_label = QLabel('Langkah-langkah:')
        self.calculate_button = QPushButton('Hitung Faktorial', self)
        self.calculate_button.setStyleSheet("background-color:red")
        self.calculate_button.clicked.connect(self.calculate_factorial)


        input_layout = QHBoxLayout()
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.input_field)

        layout = QVBoxLayout(self)
        layout.addLayout(input_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.steps_label)  # Add the steps label to the layout

        self.setLayout(layout)
        self.setGeometry(150, 150, 320, 450)  # Increased height to accommodate the steps label
        self.setWindowTitle("Factorial Calculator")
        self.setStyleSheet("""
            QWidget {
                background-color: #F0F0F0;
                color: #000000;
            }
            QLabel {
                font-size: 14px;
                color:white:
                
            }
            QLineEdit, QPushButton {
                # background-color: red;  /* Green */
                border: none;
                color: white;
                padding: 10px 15px;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;  /* Darker Green */
            }
        """)
        self.show()

    def calculate_factorial(self):
        try:
            n = int(self.input_field.text())

            if n < 0:
                QMessageBox.warning(self, 'Peringatan', 'Masukkan bilangan bulat non-negatif.')
                return

            result = 1
            steps = []
            for i in range(1, n + 1):
                result *= i

                steps.append(f'{i}x' if i != n else f'{i}')  # Store each step in the list
                print(i)
            # Display the final result and the steps
            self.result_label.setText(f'Faktorial dari {n} adalah {result}')
            self.steps_label.setText('Langkah-langkah: ' + ''.join(steps))


        except ValueError:
            QMessageBox.warning(self, 'Peringatan', 'Masukkan bilangan bulat.')

if __name__ == "__main__":
    app = QApplication([])
    factorial_app = FactorialCalculatorApp()
    app.exec()
