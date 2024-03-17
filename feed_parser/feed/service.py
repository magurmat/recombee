from .models import Feed
from feed_parser.image.service import ImageService
import threading
import uuid
from feed_parser.item.service import ItemService
from . import app
from feed_parser import db


class FeedService:

    def __init__(self):
        self.item_service = ItemService()
        self.image_service = ImageService()

    def get_feed(self, feed_id):
        with app.app_context():
            return db.session.query(Feed).filter_by(id=feed_id).first()

    def get_feed_items(self, feed_id):
        with app.app_context():
            feed = db.session.query(Feed).filter_by(id=feed_id).first()
        if feed:
            return feed.items
        else:
            return []

    def process_feed_async(self, feed_id):
        with app.app_context():
            feed = db.session.query(Feed).filter_by(id=feed_id).first()
            for item in feed.items:
                if item.image_link:
                    self.image_service.download_image(feed_id=feed_id, image_link=item.image_link)
                for id, link in item.additional_image_links.items():
                    self.image_service.download_image(feed_id=feed_id, image_link=link)

            feed.status = "DONE"
            db.session.commit()

    def parse_feed(self, xml_feed):
        feed_data = xml_feed['rss']['channel']
        items = []
        feed_id = str(uuid.uuid4())
        for item_elem in feed_data['item']:
            item = self.item_service.parse_item(xml_item=item_elem, feed_id=feed_id)
            items.append(item)
            db.session.add(item)
        feed = Feed(id=feed_id, title=feed_data['title'], description=feed_data['description'],
                    link=feed_data['link'], items=items, status="PROCESSING")
        db.session.add(feed)
        db.session.commit()
        _thread = threading.Thread(target=self.process_feed_async, args=[feed_id])
        _thread.start()
        return feed.id
