from flask import Flask
from models import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    return app


def init_db(app):
    with app.app_context():
        db.create_all()