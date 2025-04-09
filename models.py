from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    features = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    tag = db.Column(db.String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "ingredients": self.ingredients,
            "price": self.price,
            "features": self.features,
            "image_url": f"http://localhost:5000/images/{self.image}" if self.image else None,
            "tag": self.tag
        }

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    opening_hours = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "opening_hours": self.opening_hours,
            "phone_number": self.phone_number
        }
