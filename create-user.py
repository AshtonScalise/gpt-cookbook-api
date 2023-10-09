from app import create_app
from app.extensions import db
from app.model import User

app = create_app()

with app.app_context():  # This is necessary to use the application's context
    # Create new user instance
    sample_user = User(username="testuser", password="testpassword")  # Use a secure hashed password in production
    
    # Add and commit user to database
    db.session.add(sample_user)
    db.session.commit()
