# Le controller (appelé Blueprint en Flask) s'occupe de recevoir les requêtes et renvoyer les réponses

from flask import Blueprint
from grand_dataset_taches import base_de_donnees_taches

stat_bp = Blueprint('stat_bp', __name__)

@stat_bp.get('/statistics/status')
def get_task_statistics():
    status_counts = {"Terminées": 0, "En cours": 0, "En attente": 0}

    for task in base_de_donnees_taches.values():
        if task["statut"] == "DONE":
            status_counts["Terminées"] += 1
        elif task["statut"] == "IN_PROGRESS":
            status_counts["En cours"] += 1
        elif task["statut"] == "TODO":
            status_counts["En attente"] += 1

    return status_counts, 200


