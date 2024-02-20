from flask import Flask
from flask import Flask, g

from dotenv import load_dotenv
import os
from database.db import get_db


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello TasksList backend!"


@app.route('/select1')
def select1():
    db = get_db()  # Get the connection here
    cur = db.cursor()

    # perform SELECT operation using the cursor
    cur.execute("SELECT * FROM public.users")
    result = cur.fetchall()
    cur.close()
    print(str(result))

    return str(result)


@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)
