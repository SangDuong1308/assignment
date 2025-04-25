from flask import Flask
from app.extensions import db, migrate, jwt
from app.config import Config
from app.api import healthz_bp, auth_bp, transaction_bp, staff_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(healthz_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='')
    app.register_blueprint(transaction_bp, url_prefix='')
    app.register_blueprint(staff_bp, url_prefix='/staff')
    
    @app.shell_context_processor
    def make_shell_context():
        from app.models.user import User
        from app.models.token_blocklist import TokenBlocklist
        from app.models.transaction import Transaction
        return dict(app=app, db=db, User=User, TokenBlocklist=TokenBlocklist, Transaction=Transaction)

    return app