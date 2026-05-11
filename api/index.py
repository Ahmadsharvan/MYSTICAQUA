import sys
import os
from pathlib import Path

# Set up path
parent = str(Path(__file__).parent.parent)
if parent not in sys.path:
    sys.path.insert(0, parent)

# Create data directory
try:
    data_dir = os.path.join(parent, "data")
    os.makedirs(data_dir, exist_ok=True)
except Exception as e:
    print(f"Warning: Could not create data directory: {e}")

try:
    # Import the full app
    from app import app
except Exception as e:
    print(f"Error importing full app: {e}")
    # Fallback to minimal app
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def error():
        return f"<h1>Error loading app</h1><p>{str(e)}</p>", 500

