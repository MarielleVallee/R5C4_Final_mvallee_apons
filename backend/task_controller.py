# Le controller (appelé Blueprint en Flask) s'occupe de recevoir les requêtes et renvoyer les réponses

from flask import Blueprint, request
from flask_expects_json import expects_json # Vous n'en aurez pas besoin pour l'examen, gardez toutefois à l'esprit qu'il faut valider les données reçues
from datetime import datetime

from grand_dataset_taches import base_de_donnees_taches, next_id
from dto import task_dto

task_bp = Blueprint('task_bp', __name__)

@task_bp.get('/tasks')
def get_tasks():
    (offset, limit) = request.args.get(key='offset', default=0), request.args.get(key='limit', default=20)

    offset = int(offset)
    limit = int(limit)

    return list(base_de_donnees_taches.values())[offset:offset+limit]

@task_bp.get('/tasks/<string:id>')
def get_task(id):
    task = base_de_donnees_taches.get(id)
    if task is None:
        return {"error":'Task not found'}, 404

    return base_de_donnees_taches[id]

@task_bp.post('/tasks')
@expects_json(task_dto)
def create_task():
    global next_id
    task = request.json
    task['id_tache'] = next_id
    task['date_creation'] = datetime.now()
    base_de_donnees_taches[next_id] = task
    next_id = str(int(next_id) + 1)

    return task, 201

@task_bp.put('/tasks/<string:id>')
def update_task(id):
    task = base_de_donnees_taches.get(id)
    if task is None:
        return {"error":'Task not found'}, 404

    task_update = request.json
    task.update(task_update)

    return task

@task_bp.delete('/tasks/<string:id>')
def delete_task(id):
    task = base_de_donnees_taches.get(id)
    if task:
      del base_de_donnees_taches[id]

    return {}, 204
