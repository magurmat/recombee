from feed_parser import db
from . import app
from .models import Image
import os
from feed_parser.constants import IMAGE_STORE
import uuid
import requests
from urllib.parse import urlparse


class ImageService:
    def __init__(self):
        pass

    def get_feed_images(self, feed_id):
        with app.app_context():
            images = db.session.query(Image).filter_by(feed_id=feed_id).all()
            if images:
                return images
            else:
                return []

    def get_image(self, feed_id, image_id):
        with app.app_context():
            return db.session.query(Image).filter_by(id=image_id, feed_id=feed_id).first()

    def download_image(self, feed_id, image_link):
        image_id = str(uuid.uuid4())

        if not os.path.exists(IMAGE_STORE):
            os.makedirs(IMAGE_STORE)

        directory_path = os.path.join(IMAGE_STORE, feed_id)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        filename = os.path.basename(urlparse(image_link).path)
        _, extension = os.path.splitext(filename)

        filepath = os.path.join(directory_path, image_id + extension)

        response = requests.get(image_link)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded and saved to: {filepath}")
            image = Image(id=image_id, type=extension, link=image_link, feed_id=feed_id)
            db.session.add(image)
        else:
            print(f"Failed to download image from {image_link}")
