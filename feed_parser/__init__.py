from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from feed_parser.constants import DATABASE_URL
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app)
    app.app_context().push()

    from feed_parser.feed.models import Feed
    from feed_parser.item.models import Item
    from feed_parser.image.models import Image

    with app.app_context():
        db.create_all()

    return app


