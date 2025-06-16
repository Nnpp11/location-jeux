# Application de gestion de location de jeux

## Prérequis :
- Python 3 installé
- Les modules `flask` et `sqlite3`

## Installation :
1. Ouvrir un terminal dans le dossier extrait.
2. Créer une base de données avec les tables nécessaires :
   > sqlite3 database.db < schema.sql

3. Importer ta table `wp_louables` (depuis ton .sql ou via un outil comme DB Browser for SQLite).

4. Lancer l’application :
   > python app.py

5. Ouvrir un navigateur à l'adresse :
   http://localhost:5000