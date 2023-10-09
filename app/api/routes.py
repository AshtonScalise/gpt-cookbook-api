from flask import Blueprint, request, jsonify
from app.model import Recipe, Step, User  # Adjust based on your actual import paths
from app.extensions import db

api = Blueprint('api', __name__)

@api.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()

    # You might want to perform more validation on 'data' here
    if not data or not all(key in data for key in ['name', 'ingredients', 'steps', 'user_id']):
        return jsonify({"message": "Missing or invalid data"}), 400

    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_recipe = Recipe(
        name=data['name'],
        ingredients=data['ingredients'],  # you might want to serialize this if it's a list
        user_id=data['user_id']
    )

    for step_data in data['steps']:
        step = Step(
            description=step_data['description'],
            image_url=step_data.get('image_url'),  # Optional
        )
        new_recipe.steps.append(step)  # Append each Step to the Recipe's steps

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"message": "Recipe added", "recipe_id": new_recipe.id}), 201


@api.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipe_list = Recipe.query.all()  # Query all recipes

    recipes = []
    for recipe in recipe_list:
        recipe_data = {
            "id": recipe.id,
            "name": recipe.name,
            "ingredients": recipe.ingredients,  # you might want to deserialize this if it's serialized
            "user_id": recipe.user_id,
            "steps": [{"description": step.description, "image_url": step.image_url} for step in recipe.steps]
        }
        recipes.append(recipe_data)

    return jsonify({"recipes": recipes})
