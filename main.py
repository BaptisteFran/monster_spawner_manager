from core import json_manager
from core.spawn import Spawn


def main():
    json_manager.read_json_map("test_map.json")
    print("\n")
    #json_manager.modify_json_map("test_map.json", "name", "Jelling", "Jelling Guard")
    #print("\n")
    #json_manager.add_spawn('test_map.json', Spawn('jelling', 'Jelling', {'x': -74.0, 'y': -139.6, 'z': -98}, 1, 30))
    print("\n")
    #json_manager.read_json_map("test_map.json")
    json_manager.delete_spawn('test_map.json', monster_name='Jelling', position={'x': -74.0, 'y': -139.6, 'z': -98})
    print("\n")
    json_manager.read_json_map("test_map.json")


if __name__ == "__main__":
    main()