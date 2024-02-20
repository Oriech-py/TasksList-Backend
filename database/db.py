from flask import g
from dotenv import load_dotenv
import os
import urllib.parse as up
import psycopg2

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]


def get_db():
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
