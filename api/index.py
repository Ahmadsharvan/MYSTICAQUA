import sys
import os
from pathlib import Path

# Set up path
parent = str(Path(__file__).parent.parent)
if parent not in sys.path:
    sys.path.insert(0, parent)

try:
    # Create data directory
    data_dir = os.path.join(parent, "data")
    os.makedirs(data_dir, exist_ok=True)

    # Import app
    from app import app

    # WSGI application
    application = app

except Exception as e:
    # If import fails, create a minimal Flask app that returns the error
    from flask import Flask, jsonify
    application = Flask(__name__)

    @application.route('/')
    def error():
        return jsonify({
            "error": str(e),
            "type": type(e).__name__
        }), 500




