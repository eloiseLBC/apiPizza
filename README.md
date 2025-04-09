## 🍕 Pizza Cap API
Bienvenue dans l’API du projet Pizza Cap, réalisée dans le cadre du projet web de 4ᵉ année à l’ISEN.
Ce backend, développé en Python avec Flask, alimente un site web vitrine dédié aux pizzas.

L’objectif est de fournir une API RESTful permettant d’interagir avec les données du site Pizza Cap : pizzas, descriptions, prix, images, et informations sur les restaurants.

## 🎯 Objectifs
- Concevoir une architecture API RESTful propre et modulaire
- Implémenter des endpoints cohérents et testables
- Relier une base de données à un front web dynamique
- Gérer des ressources médias (images) depuis une API Flask

## 🧪 Technologies utilisées
- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-RESTful
- Flask-Migrate
- Marshmallow
- SQLite (pour l’environnement local)

## 🚀 Lancer le projet localement
### Cloner le repo
<pre>git clone https://github.com/<ton_user>/pizza-cap-api.git
cd pizza-cap-api
</pre>
  
### Installer les dépendances
<pre>pip install -r requirements.txt</pre>

### Initialiser la base de données

<pre>
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
</pre>

### (Optionnel) Charger les données depuis les fichiers JSON

<pre>python app.py   # Les données de test sont insérées au premier lancement</pre>

### Lancer le serveur
<pre>python app.py</pre>

##  📂 Structure du projet
<pre>
pizza-cap-api/
├── app.py               # Point d’entrée principal
├── models.py            # Modèles SQLAlchemy
├── routes.py            # Définition des routes Flask
├── pizza_data.json      # Données d’exemple pour les pizzas
├── restaurant_data.json # Données d’exemple pour les restaurants
├── images/              # Contient les fichiers image des pizzas
└── README.md
</pre>

## 📡 Endpoints disponibles
### 🔎 Pizzas
| Méthode | Endpoint               | Description                        |
|--------:|------------------------|------------------------------------|
| GET     | `/pizzas`              | Récupère toutes les pizzas         |
| GET     | `/pizzas/<id>`         | Récupère une pizza spécifique      |

### 🍴 Restaurants
| Méthode | Endpoint               | Description                        |
|--------:|------------------------|------------------------------------|
| GET     | `/restaurants`         | Liste les restaurants partenaires  |


## 🧾 Exemple de réponse JSON
<pre> json {
  "id": 1,
  "name": "Margherita",
  "description": "Classic pizza with tomato sauce, mozzarella, and fresh basil.",
  "ingredients": "Tomato sauce, Mozzarella, Fresh basil",
  "price": 8.5,
  "features": "Vegetarian, Gluten-free option",
  "image_url": "http://localhost:5000/images/margherita.jpeg",
  "tag": "popular"
} </pre>


## 📌 Possibles améliorations futures
- Filtrage et recherche de pizzas
- Ajout de pizzas via POST (interface admin)
- Authentification utilisateur
- Pagination et tri

