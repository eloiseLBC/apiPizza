from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from models import db, Pizza, Restaurant
from routes import register_routes
import json
import os
import socket

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzadatabase.db'

db.init_app(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
host = os.environ.get("RAILWAY_PUBLIC_DOMAIN")
if not host:
    host = f"http://localhost:{os.environ.get('PORT', 5000)}"
else:
    host = f"https://{host}"


register_routes(app)

def load_data_from_json():
    with app.app_context():
        # Création des tables si elles n'existent pas
        db.create_all()

        # On ne recharge pas si déjà des pizzas/restos en base
        if Pizza.query.first() or Restaurant.query.first():
            print("📦 Données déjà présentes, pas besoin de recharger.")
            return

        # Chargement depuis JSON
        def read_json(file):
            with open(file, 'r', encoding='utf-8') as f:
                return json.load(f)

        pizzas = read_json('pizza_data.json')
        restaurants = read_json('restaurant_data.json')

        for r in restaurants:
            r["opening_hours"] = json.dumps(r.get("opening_hours", {}))
            db.session.add(Restaurant(**r))

        for p in pizzas:
            p["ingredients"] = ", ".join(p["ingredients"]) if isinstance(p["ingredients"], list) else p["ingredients"]
            p["features"] = json.dumps(p.get("features", {}))  
            if "image" in p:
                p["image_url"] = f"{host}/static/images/{p['image']}"         
            pizza = Pizza(**p)
            db.session.add(pizza)


        db.session.commit()
        print("✅ Données JSON insérées avec succès !")

# Charger les données à la première exécution
load_data_from_json()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
