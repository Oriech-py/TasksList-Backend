"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        # from .home import routes
        from .routes import users_route

        # Register Blueprints
        # app.register_blueprint(home.home_bp)
        app.register_blueprint(routes.users_route)

        return app
