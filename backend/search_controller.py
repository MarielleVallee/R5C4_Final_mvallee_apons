from flask import Blueprint, jsonify
import json

search_bp = Blueprint('search_bp', __name__)

#Une route permettant de récupérer de manière paginée


#Une route permettant de récupérer toutes les données du fichier `searches.json`, qui sera utilisée pour la visualisation

@search_bp.get('/Allsearches')
def get_search_all():
    try:
        # Ouvrir et lire les données depuis le fichier JSON
        with open('searches.json', 'r') as file:
            searches_data = json.load(file)

        # Retourner les données lues dans une réponse JSON
        return jsonify(searches_data), 200

    except FileNotFoundError:
        # Si le fichier n'est pas trouvé, retourner une erreur 404
        return {"message": "searches.json not found"}, 404
    except json.JSONDecodeError:
        # Si le JSON est mal formé, retourner une erreur 400
        return {"message": "Error parsing JSON"}, 400

#pour la création d'une donnée
@search_bp.post('/create')
def create_search():
    return jsonify({"error": "Method not implemented"}), 501

@search_bp.put('/<string:id>')
def update(id):
    return jsonify({"error": "Method not implemented"}), 501

@search_bp.delete('/<string:id>')
def delete(id):
    return jsonify({"error": "Method not implemented"}), 501
