task_dto = {
  "type": "object",
  "properties": {
    "nom": {"type": "string"},
    "description": {"type": "string"},
    "categorie": {"type": "string"},
    "statut": {"type": "string"},
    "priorite": {"type": "string"},
    "utilisateur": {"type": "string"},
  },
  "required": ["nom", "description", "categorie", "statut", "priorite", "utilisateur"],
  "additionalProperties": False
}