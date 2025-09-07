from PyQt6.QtCore import QSize, Qt

from core import json_manager
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel,\
    QTabWidget, QGridLayout, QFormLayout, QTableWidget, QLineEdit, QTableWidgetItem, QLayout, QHBoxLayout, QVBoxLayout, \
    QHeaderView

from core.json_manager import populate_hcol_table, populate_vcol_table


def init_window():
    # Pass sys.argv to allow command line arguments for your app
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Pink Spawn Manager")
        self.read_label = QLabel()

        self.map_name = QLineEdit()
        self.map_name.setPlaceholderText("test_map")

        container = QWidget()

        main_layout = QGridLayout(container)

        self.read_label.setText("Put a map name to show all spawns")

        btn_read = QPushButton("Show all spawns")
        btn_read.clicked.connect(self.populate_map)
        btn_modify = QPushButton("Modify spawn")
        btn_add = QPushButton("Add spawn")
        btn_delete = QPushButton("Delete spawn")
        btn_save = QPushButton("Save map")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)

        show_page = QWidget()
        show_page_layout = QVBoxLayout(show_page)
        show_page.setLayout(show_page_layout)

        self.table = QTableWidget()

        table_hheaders = populate_hcol_table("test_map.json")
        table_vheaders = populate_vcol_table("test_map.json")

        self.table.setRowCount(len(table_vheaders))
        self.table.setColumnCount(len(table_hheaders))
        self.table.setVerticalHeaderLabels(table_vheaders)
        self.table.setHorizontalHeaderLabels(table_hheaders)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        tabs.addTab(show_page, "Map spawns")

        show_page_layout.addWidget(self.read_label)
        show_page_layout.addWidget(self.map_name)
        button_row = QHBoxLayout()
        button_row.addWidget(btn_read)
        button_row.addWidget(btn_add)
        button_row.addWidget(btn_modify)
        button_row.addWidget(btn_delete)
        button_row.addWidget(btn_save)
        show_page_layout.addLayout(button_row)
        show_page_layout.addWidget(self.table)

        main_layout.addWidget(tabs, 0, 0, 1, 1)
        main_layout.setRowStretch(0, 1)
        main_layout.setColumnStretch(0, 1)

        self.setCentralWidget(container)

        self.setFixedSize(QSize(1280, 800))


    def populate_map(self):
        if self.map_name.text() is None or self.map_name.text() == "":
            return
        data = json_manager.read_json_map(self.map_name.text() + ".json")

        for key in data:
            if key == "map_name":
                pass
            if key == "monster_spawns":
                row_count = 0
                for value in data[key]:
                    for cle, valeur in value.items():
                        if cle == "monster_type":
                            self.table.setItem(row_count, 0, QTableWidgetItem(valeur))
                        if cle == "name":
                            self.table.setItem(row_count, 1, QTableWidgetItem(valeur))
                        if cle == "position":
                            self.table.setItem(row_count, 2, QTableWidgetItem(str(valeur)))
                        if cle == "level":
                            self.table.setItem(row_count, 3, QTableWidgetItem(str(valeur)))
                        if cle == "respawn_time":
                            self.table.setItem(row_count, 4, QTableWidgetItem(str(valeur)))
                    row_count += 1
