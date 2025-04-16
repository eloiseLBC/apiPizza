from flask import jsonify, send_from_directory
from models import Pizza, Restaurant
import os

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

    # @app.route('/images/<path:filename>', methods=['GET'])
    # def serve_image(filename):
    #     return send_from_directory(os.path.join(app.root_path, 'images'), filename, mimetype='image/jpeg')
