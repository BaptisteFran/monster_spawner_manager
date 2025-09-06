from core import json_manager
from core.spawn import Spawn
from ui import main_window


def main():
    main_window.init_window()
    #json_manager.modify_json_map("test_map.json", "name", "Jelling", "Jelling Guard")
    #json_manager.add_spawn('test_map.json', Spawn('jelling', 'Jelling', {'x': -74.0, 'y': -139.6, 'z': -98}, 1, 30))
    #json_manager.delete_spawn('test_map.json', monster_name='Jelling', position={'x': -74.0, 'y': -139.6, 'z': -98})


if __name__ == "__main__":
    main()