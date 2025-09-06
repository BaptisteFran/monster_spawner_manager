import json
import os

from core.spawn import Spawn


def read_json_map(file: str):
    full_path = os.path.join("./data/" + file)
    with open(full_path) as f:
        game_map = json.load(f)

        for key in game_map.keys():
            if key == 'monster_spawns':
                for monster_spawn in game_map[key]:
                    print(monster_spawn)


def modify_json_map(file: str, attribute: str, old_value: str, new_value: str):
    full_path = os.path.join("./data/" + file)
    with open(full_path) as read_file:
        game_map = json.load(read_file)

        for key in game_map.keys():
            if key == 'monster_spawns':
                for monster_spawn in game_map[key]:
                    if monster_spawn[attribute] == old_value:
                        monster_spawn[attribute] = new_value

        with open(full_path, 'w') as write_file:
            json.dump(map, write_file)


def add_spawn(file: str, spawn: Spawn):
    print(spawn)
    full_path = os.path.join("./data/" + file)
    with open(full_path) as read_file:
        game_map = json.load(read_file)

        for key in game_map.keys():
            if key == 'monster_spawns':
                game_map[key].append(spawn)