import json
import os

from core.spawn import Spawn


def read_json_map(file: str):
    full_path = os.path.join("./data/" + file)
    with open(full_path) as f:
        data = json.load(f)

        if data is None:
            return None

        spawns = [
            Spawn.from_dict(spawn_dict)
            for spawn_dict in data.get("monster_spawns", [])
        ]

        return {
            "map_name": data.get("map_name", ""),
            "monster_spawns": spawns
        }


def save_map(map_name: str, data: dict):
    full_path = os.path.join("./data/" + map_name + ".json")
    with open(full_path, 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file)


def display_maps():
    maps = []
    path = os.path.join("./data/")
    for file in os.listdir(path):
        if file.endswith(".json"):
            maps.append(file)

    spawn_nb = []
    maps_avg = []
    for map_name in maps:
        data = read_json_map(map_name)
        for key in data:
            if key == "monster_spawns":
                average_level = []
                spawn_nb.append(data[key])
                for monster_spawn in data[key]:
                    average_level.append(monster_spawn.level)
                if len(average_level) > 0:
                    maps_avg.append(int(round(sum(average_level) / len(average_level))))
                else:
                    maps_avg.append(0)


    return {"maps": maps, "spawns": spawn_nb, "maps_avg": maps_avg}


def add_new_map(map_name: str):
    path = os.path.join("./data/" + map_name + ".json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({
            "map_name": map_name,
            "monster_spawns": []
        }, f)

def delete_map(map_name: str):
    path = os.path.join("./data/" + map_name)
    os.remove(path)
