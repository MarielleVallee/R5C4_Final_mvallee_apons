search_dto = {
  "type": "object",
  "properties": {
    "id": 1,
    "algorithm": "Djikstra",
    "grid_width": 10,
    "grid_height": 10,
    "move_type": "orthogonal",
    "start": [0, 0],
    "end": [9, 9],
    "path_length": 18,
    "visited_nodes": 100,
    "time_ns": 1500
  },
   "required": ["id", "algorithm", "grid_width", "grid_height", "move_type", "start", "end", "path_length", "visited_nodes", "time_ns"]
}