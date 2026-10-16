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