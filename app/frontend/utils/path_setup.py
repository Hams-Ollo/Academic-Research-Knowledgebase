import os
import sys

def add_project_root_to_path():
    """Add the project root directory to Python path."""
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
