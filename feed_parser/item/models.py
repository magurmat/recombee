from sqlalchemy import JSON
from dataclasses import dataclass
from feed_parser import db


@dataclass
class Item(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    external_id = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(10000))
    link = db.Column(db.String(100))
    image_link = db.Column(db.String(100))
    additional_image_links = db.Column(JSON, nullable=False)
    price = db.Column(db.String(100))
    condition = db.Column(db.String(100))
    availability = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    gtin = db.Column(db.String(100))
    item_group_id = db.Column(db.String(100))
    sale_price = db.Column(db.String(100))
    feed_id = db.Column(db.String, db.ForeignKey('feed.id'), nullable=False)

    def __init__(self, id, external_id, title, description, link, image_link, additional_image_links, price, condition,
                 availability,
                 brand, gtin, item_group_id, sale_price, feed_id):
        self.id = id
        self.external_id = external_id
        self.title = title
        self.description = description
        self.link = link
        self.image_link = image_link
        self.additional_image_links = additional_image_links
        self.price = price
        self.condition = condition
        self.availability = availability
        self.brand = brand
        self.gtin = gtin
        self.item_group_id = item_group_id
        self.sale_price = sale_price
        self.feed_id = feed_id

    def to_dict(self):
        return {
            'id': self.id,
            'external_id': self.external_id,
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'image_link': self.image_link,
            'additional_image_links': self.additional_image_links,
            'price': self.price,
            'condition': self.condition,
            'availability': self.availability,
            'brand': self.brand,
            'gtin': self.gtin,
            'item_group_id': self.item_group_id,
            'sale_price': self.sale_price,
            'feed_id': self.feed_id
        }