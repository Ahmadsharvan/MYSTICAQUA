import sys
import os
from pathlib import Path

# Set up path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import Flask app
from app import app

# Export the app for Vercel
__all__ = ['app']


