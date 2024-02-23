from flask import Blueprint
from database import db as DB


users_route = Blueprint('users_route', __name__)


@users_route.route('/users/add_user', methods=["GET", "POST"])
def add_user():
    return "nice"


@users_route.route('/users', methods=["GET", "POST"])
def get_users():

    with DB.get_db() as db:  # Get the connection

        with db.cursor() as cur:  # Init the cursor

            # perform SELECT operation using the cursor
            cur.execute("SELECT * FROM public.users")
            result = cur.fetchall()
            cur.close()
            print(str(result))

            return str(result)
    # return "get_users()"
