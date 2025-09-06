import json
import os

from core.spawn import Spawn


def read_json_map(file: str):
    full_path = os.path.join("./data/" + file)
    with open(full_path) as f:
        game_map = json.load(f)

        if game_map is None:
            return

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
    full_path = os.path.join("./data/" + file)
    with open(full_path) as read_file:
        game_map = json.load(read_file)

        for key in game_map.keys():
            if key == 'monster_spawns':
                game_map[key].append(spawn.__dict__)

    with open(full_path, 'w') as write_file:
        json.dump(game_map, write_file)


def delete_spawn(file: str, monster_name: str, position: dict):
    not_in_map = True
    full_path = os.path.join("./data/" + file)
    with open(full_path) as read_file:
        game_map = json.load(read_file)

        for key in game_map.keys():
            if key == 'monster_spawns':
                for monster_spawn in game_map[key]:
                    if monster_spawn["name"] == monster_name and monster_spawn["position"] == position:
                        not_in_map = False
                        game_map[key].remove(monster_spawn)

        if not_in_map:
            print("Spawn not found")

    with open(full_path, 'w') as write_file:
        json.dump(game_map, write_file)