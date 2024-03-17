from feed_parser.feed.service import FeedService
from feed_parser.item.service import ItemService
from feed_parser.image.service import ImageService
from flask import request, jsonify, send_file, Blueprint, make_response
import xmltodict
import os
from feed_parser.constants import IMAGE_STORE

api = Blueprint('api', __name__)
item_service = ItemService()
feed_service = FeedService()
image_service = ImageService()


@api.route('/feeds', methods=['POST'])
def parse_xml():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/xml':
        error_message = {"error": "Invalid Content-Type. Must be application/xml."}
        return make_response(jsonify(error_message), 400)
    try:
        xml_data = request.data
        data_dict = xmltodict.parse(xml_data)
        return make_response(jsonify({"id": feed_service.parse_feed(data_dict)}),201)
    except Exception as e:
        error_message = {"error": str(e)}
        return make_response(jsonify(error_message), 400)


@api.route('/feeds/<feed_id>', methods=['GET'])
def get_feed_status_by_id(feed_id):
    feed = feed_service.get_feed(feed_id)

    if feed:
        return jsonify({"status": feed.status})

    return "Feed not found", 404


@api.route('/feeds/<feed_id>/items', methods=['GET'])
def get_feed_items_by_id(feed_id):
    items = feed_service.get_feed_items(feed_id)

    if items:
        return jsonify({"ids": [item.id for item in items]})

    return "Feed not found", 404


@api.route('/feeds/<feed_id>/images', methods=['GET'])
def get_feed_images_by_id(feed_id):
    images = image_service.get_feed_images(feed_id)

    if images:
        return jsonify({"ids": [image.id for image in images]})

    return "Feed not found", 404


@api.route('/feeds/<feed_id>/items/<item_id>', methods=['GET'])
def get_item_by_id_and_feed_id(feed_id, item_id):
    item = item_service.get_item(feed_id=feed_id, item_id=item_id)

    if item:
        return jsonify(item.to_dict())

    return "Item not found", 404


@api.route('/feeds/<feed_id>/images/<image_id>', methods=['GET'])
def get_image_by_id_and_feed_id(feed_id, image_id):
    image = image_service.get_image(feed_id=feed_id, image_id=image_id)

    if image:
        filepath = os.path.join(IMAGE_STORE, feed_id, f"{image.id}{image.type}")
        return send_file(filepath, mimetype=f"image/{image.type[1:]}")

    return "Image not found", 404
