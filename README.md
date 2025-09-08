# Spawn Manager Tool

This is a **spawn manager tool** I made for my in-development MMORPG.  
It is built using **PyQt6** and Python standard libraries.

## Features

- **Manage Spawns**
  - Show every spawn for a map
  - Add a spawn
  - Modify a spawn
  - Delete a spawn

- **Manage Maps**
  - Add a map
  - Delete a map

## Map Format

Maps are stored in **JSON format**. Example:

```json
{
  "map_name": "test_map",
  "monster_spawns": [
    {
      "monster_type": "test",
      "name": "Test Monster",
      "position": {
        "x": -72.0,
        "y": -139.6,
        "z": -95.0
      },
      "level": 1,
      "respawn_time": 30
    }
  ]
}
```

Python version :
  Python 3.13.5

Can be used with Python >= 3.9 
This project uses UV
