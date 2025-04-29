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
        return jsonify([p.serialize() for p in pizzas]), 200

    @app.route('/pizzas/<int:pizza_id>', methods=['GET'])
    def get_pizza(pizza_id):
        pizza = Pizza.query.get_or_404(pizza_id)
        return jsonify(pizza.serialize()), 200
    
    
    
