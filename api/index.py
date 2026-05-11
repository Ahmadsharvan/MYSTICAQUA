import sys
import os
from pathlib import Path

# Set up path
parent = str(Path(__file__).parent.parent)
if parent not in sys.path:
    sys.path.insert(0, parent)

# Create data directory
data_dir = os.path.join(parent, "data")
os.makedirs(data_dir, exist_ok=True)

try:
    from app import app
    application = app

except Exception as e:
    import traceback
    error_msg = str(e)
    traceback_str = traceback.format_exc()

    # Create minimal Flask app that shows the error
    from flask import Flask, jsonify
    application = Flask(__name__)

    @application.route('/')
    @application.route('/api/<path:path>')
    def show_error(path=''):
        return jsonify({
            "error": "Failed to load main application",
            "message": error_msg,
            "type": type(e).__name__,
            "traceback": traceback_str
        }), 500





