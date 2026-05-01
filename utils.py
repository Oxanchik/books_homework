import os

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()
PASS = os.getenv("PASS")

def create_database_if_not_exists(db_name):
    """Создает базу данных, если она не существует"""

    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password=PASS,
        database="postgres"
    )

    try:
        conn.autocommit = True

        with conn.cursor() as cur_db:
            cur_db.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
            exists = cur_db.fetchone()

            if not exists:
                cur_db.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                print(f"✅ База данных '{db_name}' создана")
            else:
                print(f"ℹ️ База данных '{db_name}' уже существует")

    finally:
        conn.close()