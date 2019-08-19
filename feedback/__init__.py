from .routes.main import main
from flask_wtf.csrf import CSRFError
from flask import Flask, render_template
from .extensions import db, migrate, csrf


def page_not_found(e):
    return render_template('404.html', reason=e.description), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    # add config file to app config
    app.config.from_pyfile(config_file)
    # Init db
    db.init_app(app)
    # Init csrf
    csrf.init_app(app)
    # Init migrate
    migrate.init_app(app, db)
    # Register blueprint
    app.register_blueprint(main)
    # Handle csrf error
    app.register_error_handler(CSRFError, csrf_error)
    # Handle 404 error
    app.register_error_handler(404, page_not_found)
    # Handle 500 error
    app.register_error_handler(500, internal_server_error)
    return app


if __name__ == '__main__':
    create_app()
