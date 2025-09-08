class Spawn:
    def __init__(self, monster_type: str, name: str, position: dict, level: int, respawn_time: int):
        self.monster_type = monster_type
        self.name = name
        self.position = position
        self.level = level
        self.respawn_time = respawn_time


    def to_dict(self):
        return {
            "monster_type": self.monster_type,
            "name": self.name,
            "position": self.position,
            "level": self.level,
            "respawn_time": self.respawn_time,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["monster_type"],
            data["name"],
            data["position"],
            data["level"],
            data["respawn_time"],
        )