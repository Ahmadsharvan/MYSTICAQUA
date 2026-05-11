import sys
import os

# Set up path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create data directory
try:
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
except Exception as e:
    pass

try:
    from app import app as flask_app
    app = flask_app
    application = flask_app
except Exception as e:
    from flask import Flask
    app = Flask(__name__)
    application = app

    @app.route('/')
    def error():
        return f"Error: {str(e)}", 500

