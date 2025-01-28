from flask import Flask
from flask_login import LoginManager
from Backend.models import db
from Backend.routes import main_routes
from Backend.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from Backend.models import User  # Import User model for user loader

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Register blueprints
app.register_blueprint(main_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)