from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    recipes = db.relationship('Recipe', backref='user', lazy=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)  # You might want to store ingredients as a JSON or a serialized list
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    steps = db.relationship('Step', backref='recipe', lazy=True)  # One-to-many relationship with Step

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500))  # Adjust string length as needed
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)  # Foreign key referencing Recipe

