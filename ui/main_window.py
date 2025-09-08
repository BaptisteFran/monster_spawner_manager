import json
import os

from PyQt6.QtCore import QSize, Qt

from core import json_manager
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel,\
    QTabWidget, QGridLayout, QFormLayout, QTableWidget, QLineEdit, QTableWidgetItem, QLayout, QHBoxLayout, QVBoxLayout, \
    QHeaderView

from core.spawn import Spawn


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

        self.new_map_name = QLineEdit()
        self.new_map_name.setPlaceholderText("new_map")

        container = QWidget()

        main_layout = QGridLayout(container)

        self.read_label.setText("Put a map name to show all spawns")

        btn_read = QPushButton("Show all spawns")
        btn_read.clicked.connect(self.populate_map)
        btn_add = QPushButton("Add spawn")
        btn_add.clicked.connect(self.add_spawn)
        btn_delete = QPushButton("Delete spawn")
        btn_delete.clicked.connect(self.delete_spawn)
        btn_save = QPushButton("Save map")
        btn_save.clicked.connect(self.save_spawn_from_table)

        btn_show_maps = QPushButton("Show maps")
        btn_show_maps.clicked.connect(self.show_maps)
        btn_new_map = QPushButton("Save new map")
        btn_new_map.clicked.connect(self.add_new_map)
        btn_delete_map = QPushButton("Delete map")
        btn_delete_map.clicked.connect(self.delete_map)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)

        show_page = QWidget()
        show_page_layout = QVBoxLayout(show_page)
        show_page.setLayout(show_page_layout)

        manage_map = QWidget()
        manage_map_layout = QVBoxLayout(manage_map)
        manage_map.setLayout(manage_map_layout)

        self.table = QTableWidget()

        table_hheaders = ["monster_type", "name", "position", "level", "respawn_time"]

        self.table.setColumnCount(len(table_hheaders))
        self.table.setHorizontalHeaderLabels(table_hheaders)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        tabs.addTab(show_page, "Map spawns")
        tabs.addTab(manage_map, "Manage Maps")

        show_page_layout.addWidget(self.read_label)
        show_page_layout.addWidget(self.map_name)
        button_row = QHBoxLayout()
        button_row.addWidget(btn_read)
        button_row.addWidget(btn_add)
        button_row.addWidget(btn_delete)
        button_row.addWidget(btn_save)
        show_page_layout.addLayout(button_row)
        show_page_layout.addWidget(self.table)

        self.map_table = QTableWidget()

        map_table_hheaders = ["name", "spawns", "average_level"]
        self.map_table.setColumnCount(len(map_table_hheaders))
        self.map_table.setHorizontalHeaderLabels(map_table_hheaders)
        self.map_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        manage_map_layout.addWidget(self.new_map_name)
        button_row = QHBoxLayout()
        button_row.addWidget(btn_show_maps)
        button_row.addWidget(btn_new_map)
        button_row.addWidget(btn_delete_map)
        manage_map_layout.addLayout(button_row)
        manage_map_layout.addWidget(self.map_table)

        main_layout.addWidget(tabs, 0, 0, 1, 1)
        main_layout.setRowStretch(0, 1)
        main_layout.setColumnStretch(0, 1)

        self.setCentralWidget(container)

        self.setFixedSize(QSize(1280, 800))

        self.data = None
        self.map_data = None


    def populate_map(self):
        if self.map_name.text() is None or self.map_name.text() == "":
            return
        self.data = json_manager.read_json_map(self.map_name.text() + ".json")

        monster_spawns = self.data.get("monster_spawns", [])
        self.table.setRowCount(len(monster_spawns))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["monster_type", "name", "position", "level", "respawn_time"])

        for row, spawn in enumerate(monster_spawns):
            self.table.setItem(row, 0, QTableWidgetItem(spawn.monster_type))
            self.table.setItem(row, 1, QTableWidgetItem(spawn.name))
            self.table.setItem(row, 2, QTableWidgetItem(f"{spawn.position['x']},{spawn.position['y']},{spawn.position['z']}"))
            self.table.setItem(row, 3, QTableWidgetItem(str(spawn.level)))
            self.table.setItem(row, 4, QTableWidgetItem(str(spawn.respawn_time)))

        self.table.itemChanged.connect(self.update_spawn_from_table)


    def update_spawn_from_table(self, item):
        row = item.row()
        col = item.column()

        spawn = self.data["monster_spawns"][row]

        if col == 0:
            spawn.monster_type = item.text()
        elif col == 1:
            spawn.name = item.text()
        elif col == 2:
            try:
                x, y, z = map(float, item.text().split(","))
                spawn.position = {"x": x, "y": y, "z": z}
            except ValueError:
                pass
        elif col == 3:
            spawn.level = int(item.text())
        elif col == 4:
            spawn.respawn_time = int(item.text())


    def add_spawn(self):
        new_spawn = Spawn(
            'monster',
            'New monster',
            {'x': 0.0, 'y': 0.0, 'z': 0.0},
            1,
            30)

        self.data["monster_spawns"].append(new_spawn)

        row = self.table.rowCount()
        self.table.setRowCount(row + 1)

        self.table.setItem(row, 0, QTableWidgetItem(new_spawn.monster_type))
        self.table.setItem(row, 1, QTableWidgetItem(new_spawn.name))
        self.table.setItem(row, 2, QTableWidgetItem(f"{new_spawn.position['x']},{new_spawn.position['y']},{new_spawn.position['z']}"))
        self.table.setItem(row, 3, QTableWidgetItem(str(new_spawn.level)))
        self.table.setItem(row, 4, QTableWidgetItem(str(new_spawn.respawn_time)))


    def delete_spawn(self):
        self.data["monster_spawns"].remove(self.data["monster_spawns"][self.table.currentRow()])
        self.table.removeRow(self.table.currentRow())


    def save_spawn_from_table(self):
        if not self.map_name.text():
            return

        data_to_save = {
            "map_name": self.map_name.text(),
            "monster_spawns": [
                spawn.to_dict() for spawn in self.data["monster_spawns"]
            ]
        }

        json_manager.save_map(self.map_name.text(), data_to_save)


    def show_maps(self):
        self.map_data = json_manager.display_maps()
        self.map_table.setRowCount(len(self.map_data["maps"]))
        for row, map_name in enumerate(self.map_data["maps"]):
            self.map_table.setItem(row, 0, QTableWidgetItem(map_name))
        for row, spawn in enumerate(self.map_data["spawns"]):
            self.map_table.setItem(row, 1, QTableWidgetItem(str(len(spawn))))
        for row, avg in enumerate(self.map_data["maps_avg"]):
            self.map_table.setItem(row, 2, QTableWidgetItem(str(avg)))

    def add_new_map(self):
        json_manager.add_new_map(self.new_map_name.text())
        self.show_maps()

    def delete_map(self):
        json_manager.delete_map(self.map_data["maps"][self.map_table.currentRow()])
        self.show_maps()


