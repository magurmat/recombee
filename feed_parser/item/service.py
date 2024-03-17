from .models import Item
import uuid
from feed_parser import db
from . import app


class ItemService():
    def __init__(self):
        pass

    def get_item(self, feed_id, item_id):
        with app.app_context():
            return db.session.query(Item).filter_by(id=item_id, feed_id=feed_id).first()

    def parse_item(self, xml_item, feed_id):
        id = xml_item['g:id']
        title = xml_item['title']
        description = xml_item['description']
        link = xml_item['link']
        image_link = xml_item['g:image_link']
        additional_image_links = xml_item.get('g:additional_image_link', [])
        additional_image_dict = {}
        if not isinstance(additional_image_links, dict):
            if not isinstance(additional_image_links, list):
                additional_image_links = [additional_image_links]
            # Generate UUIDs for each link and store them in the dictionary
            for link in additional_image_links:
                image_uuid = str(uuid.uuid4())
                additional_image_dict[image_uuid] = link
        price = xml_item['g:price']
        condition = xml_item['g:condition']
        availability = xml_item['g:availability']
        brand = xml_item['g:brand']
        gtin = xml_item['g:gtin']
        item_group_id = xml_item['g:item_group_id']
        sale_price = xml_item.get('g:sale_price')
        return Item(id=str(uuid.uuid4()), external_id=id, title=title, description=description, link=link,
                    image_link=image_link, additional_image_links=additional_image_dict, price=price,
                    condition=condition, availability=availability, brand=brand, gtin=gtin,
                    item_group_id=item_group_id, sale_price=sale_price, feed_id=feed_id)
