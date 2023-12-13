from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

class FactorialDefinitionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        definition_label = QLabel(
            "Factorial adalah hasil dari perkalian semua bilangan bulat positif atau non-negatif dari 1 hingga suatu bilangan tertentu. "
            "Cara menentukan nilai faktorial suatu bilangan (n) adalah sebagai berikut:\n"
            "1. Kalikan semua bilangan bulat dari 1 hingga n.\n"
            "2. Hasilnya adalah faktorial dari n."
        )
        definition_label.setMaximumWidth(280)  # Set the maximum width for the label
        definition_label.setWordWrap(True)  # Allow text to wrap within the label


        self.image_label = QLabel(self)
        pixmap = QPixmap('factorial.png')
        pixmap = pixmap.scaledToWidth(300)  # Set the width of the image
        self.image_label.setPixmap(pixmap)
        self.image_label.setStyleSheet("background-color:white")


        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)  # Add the image label to the layout
        layout.addWidget(definition_label)

        self.setLayout(layout)


        # Apply a custom stylesheet for a stylish appearance
        self.setStyleSheet("""
                    QWidget {
                        background-color: #2E2E2E;
                        color: #FFFFFF;
                    }
                    QLabel {
                        font-size: 14px;
                    }
                    
                """)

if __name__ == '__main__':
    app = QApplication([])
    definition_window = FactorialDefinitionApp()
    definition_window.show()
    app.exec()
