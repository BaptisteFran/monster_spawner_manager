import json


class Spawn:
    def __init__(self, monster_type: str, name: str, position: dict, level: int, respawn_time: int):
        self.monster_type = monster_type
        self.name = name
        self.position = position
        self.level = level
        self.respawn_time = respawn_time


class SpawnEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__