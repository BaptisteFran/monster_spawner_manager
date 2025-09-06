from PyQt6.QtCore import QSize, Qt

from core import json_manager
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel,\
    QTabWidget, QGridLayout, QFormLayout, QTableWidget, QLineEdit, QTableWidgetItem, QLayout, QHBoxLayout, QVBoxLayout, \
    QHeaderView

from core.json_manager import read_json_map, populate_hcol_table, populate_vcol_table


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
        self.add_label = QLabel()
        self.modify_label = QLabel()
        self.delete_label = QLabel()

        self.map_name = QLineEdit()
        self.map_name.setPlaceholderText("test_map")

        container = QWidget()

        main_layout = QGridLayout(container)

        self.read_label.setText("Show existing spawns")
        self.add_label.setText("Add new spawn")
        self.modify_label.setText("Modify existing spawn")
        self.delete_label.setText("Delete existing spawn")

        btn_read = QPushButton("Show all spawns")
        btn_read.clicked.connect(self.populate_map)

        btn_modify = QPushButton("Modify spawn")
        btn_add = QPushButton("Add spawn")
        btn_delete = QPushButton("Delete spawn")

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

        add_page = QWidget()
        add_page_layout = QVBoxLayout(add_page)
        add_page.setLayout(add_page_layout)

        modify_page = QWidget()
        modify_page_layout = QVBoxLayout(modify_page)
        modify_page.setLayout(modify_page_layout)

        delete_page = QWidget()
        delete_page_layout = QVBoxLayout(delete_page)
        delete_page.setLayout(delete_page_layout)

        tabs.addTab(show_page, "Map spawns")
        tabs.addTab(add_page, "Add spawn")
        tabs.addTab(modify_page, "Modify spawn")
        tabs.addTab(delete_page, "Delete spawn")

        show_page_layout.addWidget(self.read_label)
        show_page_layout.addWidget(self.map_name)
        show_page_layout.addWidget(btn_read)
        show_page_layout.addWidget(self.table)

        add_page_layout.addWidget(self.add_label)
        add_page_layout.addWidget(btn_add)

        modify_page_layout.addWidget(self.modify_label)
        modify_page_layout.addWidget(btn_modify)

        delete_page_layout.addWidget(self.delete_label)
        delete_page_layout.addWidget(btn_delete)

        main_layout.addWidget(tabs, 0, 0, 1, 1)
        main_layout.setRowStretch(0, 1)
        main_layout.setColumnStretch(0, 1)

        self.setCentralWidget(container)

        self.setFixedSize(QSize(1024, 960))


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
                            position = ""
                            for i,k in valeur.items():
                                position = position + " " + str(k)
                            self.table.setItem(row_count, 2, QTableWidgetItem(position))
                        if cle == "level":
                            self.table.setItem(row_count, 3, QTableWidgetItem(str(valeur)))
                        if cle == "respawn_time":
                            self.table.setItem(row_count, 4, QTableWidgetItem(str(valeur)))
                    row_count += 1
