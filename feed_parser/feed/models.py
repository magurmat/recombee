from feed_parser import db


class Feed(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(10000))
    link = db.Column(db.String(100))
    items = db.relationship('Item', backref='feed', lazy='subquery')
    status = db.Column(db.String(100))

    def __init__(self, id, title, description, link, items, status):
        self.id = id
        self.title = title
        self.description = description
        self.link = link
        self.items = items
        self.status = status
