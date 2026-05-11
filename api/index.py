import sys
import os
from pathlib import Path

# Set up path to import from parent directory
parent = str(Path(__file__).parent.parent)
if parent not in sys.path:
    sys.path.insert(0, parent)

# Ensure data directory exists
data_dir = os.path.join(parent, "data")
os.makedirs(data_dir, exist_ok=True)

# Import and configure Flask app
from app import app

# This is the WSGI application that Vercel calls
application = app
app.wsgi_app = app.wsgi_app



