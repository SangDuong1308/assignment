from flask import Flask
from app.extensions import db, migrate, jwt
from app.config import Config
from app.api import healthz_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(healthz_bp, url_prefix='/')

    return app