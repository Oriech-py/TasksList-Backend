from flask import Flask, g

from dotenv import load_dotenv
import os
from database.db import create_tables, get_db
from routes.users_route import users_route


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


app = Flask(__name__)


app.register_blueprint(users_route)


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


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()


def init_app():
    # ...

    tables_created = os.getenv("TABLES_CREATED")

    if tables_created == "False":
        with app.app_context():
            # db = get_db()
            create_tables()


if __name__ == "__main__":
    init_app()
    app.run(debug=True)
