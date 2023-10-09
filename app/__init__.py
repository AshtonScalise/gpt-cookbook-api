from flask import Flask
from .config import Config  # Importing Config class from config.py
from .extensions import db, jwt  # Assuming you have db and jwt initialized in extensions.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Set configuration from Config class

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Registering Blueprint (you need to create Blueprint in routes.py)
    from app.api.routes import api  # Adjust path if necessary
    app.register_blueprint(api, url_prefix='/api')

    return app

# Here you can add other initializations, configurations, or set up other Blueprints as necessary.
