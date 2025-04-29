from flask import jsonify
from models import Pizza, Restaurant
import json

def register_routes(app):

    @app.route('/restaurants', methods=['GET'])
    def list_restaurants():
        restaurants = Restaurant.query.all()
        return jsonify([r.serialize() for r in restaurants]), 200

    @app.route('/pizzas', methods=['GET'])
    def list_pizzas():
        pizzas = Pizza.query.all()
        result = []
        for pizza in pizzas:
            pizza_data = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients,
                'image_url': pizza.image_url,
                'price': pizza.price,
                'tag': pizza.tag,
                'categorie': pizza.categorie,
                'features': json.loads(pizza.features) if pizza.features else {}
            }
            result.append(pizza_data), 200
        return jsonify(result)

    @app.route('/pizzas/<int:pizza_id>', methods=['GET'])
    def get_pizza(pizza_id):
        pizza = Pizza.query.get_or_404(pizza_id)
        pizza_data = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients,
                'image_url': pizza.image_url,
                'price': pizza.price,
                'features': json.loads(pizza.features) if pizza.features else {}
            }
        return jsonify(pizza_data), 200