from core import json_manager
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout


def btn_read_json():
    json_manager.read_json_map("test_map.json")

def init_window():
    # Pass sys.argv to allow command line arguments for your app
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Pink Sapwn Manager")
        self.label = QLabel()
        self.input = QLineEdit()

        self.label.setText("Show existing spawns")

        btn_read = QPushButton("Read JSON")
        btn_read.clicked.connect(btn_read_json)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(btn_read)

        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)

        self.setFixedSize(800, 600)