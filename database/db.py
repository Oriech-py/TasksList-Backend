from flask import g, current_app
from dotenv import load_dotenv
import os
import urllib.parse as up
import psycopg2


# from db_tables import create_tables_queries

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]


def get_db():
    """
    Establishing the DB connection using psycopg2,
    and updating the global.
    """
    with current_app.app_context():

        if 'db' not in g:
            # init db connection
            up.uses_netloc.append("postgres")
            url = up.urlparse(DATABASE_URL)

            g.db = psycopg2.connect(database=url.path[1:],
                                    user=url.username,
                                    password=url.password,
                                    host=url.hostname,
                                    port=url.port
                                    )

            return g.db


# Ensure the app instance is available before calling get_db()

    # get_db()


def create_tables():
    """
    This function being called when environment variable is set to Flase.
    It creates the tables in the DB, provided by an import from db_tables.py.
    """
    from db_tables import create_tables_queries

    with get_db() as conn:

        with conn.cursor() as cur:

            for create_table in create_tables_queries:
                print(f'create_table: {create_table}')
                cur.execute(create_table)

            conn.commit()
        # conn.close() - Butal
