from flask import Flask
from .routes import bp as main_bp
import os

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register the blueprint
    app.register_blueprint(main_bp)

    return app
