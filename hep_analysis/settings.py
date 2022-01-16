"""
Settings for HEP Analysis Project.

"""
import os
from pathlib import Path

# BASE_DIR is the top directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# connection string to sqlite database
DB_PATH =  os.path.join(BASE_DIR, 'db.sqlite3')
DB_CONNECTION_STRING  = "sqlite:///" + DB_PATH

print(BASE_DIR)