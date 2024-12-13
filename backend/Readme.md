# Installation du projet

- Créer un venv et l'activer (optionnel)
- Installer les dépendances contenues dans requirements.txt avec `pip install -r requirements.txt`

# Lancement

- Une fois les dépendances installées, le projet peut être lancé avec `flask run`
- Pour une version de développement, utiliser `flask run --debug`

# Architecture du projet

- app.py: initialise l'application et importe les controllers
- \*\_controller.py: groupe les routes pour un endpoint défini
- dto.py: contient le code pour la validation des body entrants selon la spécification de flask_expects_json
- grand_dataset_taches.py: données db mockées

# Packages importants

- flask: framework utilisé
- flask_cors: pour permettre la configuration des options CORS et connecter l'appli au frontend
- flask_expects_json: pour la validation des données entrantes (POST / PUT)

# Routes Principales

- tasks

  - GET /
    - Query: offset (int) et pagination (int)
  - GET /:id
  - POST /
  - PUT /:id
  - DELETE /:id

- statistics
  - GET /status
