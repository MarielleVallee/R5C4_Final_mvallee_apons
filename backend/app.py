from flask import Flask, jsonify
from flask_cors import CORS
from search_controller import search_bp

app = Flask(__name__)

# Attention, si vous faites tourner le code sur un pc de l'IUT, il est possible que vous deviez 
# impérativement préciser l'origine autorisée, c'est à dire le port occupé par votre front, au lieu du "*"
#CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

# votre fichier app ne devrait pas contenir de routes, seulement les imports et l'instanciation de l'application...
app.register_blueprint(search_bp)

# ...à l'exception d'un hello world éventuellement
@app.get('/')
def hello():
    return {"message": 'Hello, World!'}, 200

# Attention, selon la version de Flask, il est possible que @app.get ne fonctionne pas
# dans ce cas, utilisez @app.route('/', methods=['GET'])
# valable pour tous les verbes HTTP 

# Toujours selon la version de Flask, il est possible qu'il refuse de retourner une liste ou un dictionnaire
# sans faire de conversion, dans ce cas, utilisez jsonify, de la manière suivante:

''' 
from flask import jsonify

app = Flask(__name__)

@app.get('/')
def hello():
    return jsonify({"message": 'Hello, World!'}), 200
'''

