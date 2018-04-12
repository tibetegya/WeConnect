# local imports
from apis import db
from apis.v2.models.user import *


class ReviewModel(db.Model):
    """Class to create a Review class object"""

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    body = db.Column(db.String(256), nullable=False)
    business = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def __init__(self, title, body, business):
        self.title = title
        self.body = body
        self.business = business
        # self.author = session["user_id"]

    def __repr__(self):
        return '<Review: {}>'.format(self.name)
