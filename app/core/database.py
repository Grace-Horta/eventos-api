import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")

    def get_connection(self):
        return psycopg2.connect(self.db_url, cursor_factory=RealDictCursor)

# Función adicional para que los repositorios que usan get_db_connection funcionen sin error
def get_db_connection():
    db_url = os.getenv("DATABASE_URL")
    return psycopg2.connect(db_url, cursor_factory=RealDictCursor)
