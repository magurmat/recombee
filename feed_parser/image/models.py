from feed_parser import db


class Image(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    feed_id = db.Column(db.String(100))
    type = db.Column(db.String(100))
    link = db.Column(db.String(100))

    def __init__(self, id, feed_id, type, link):
        self.id = id
        self.feed_id = feed_id
        self.type = type
        self.link = link
