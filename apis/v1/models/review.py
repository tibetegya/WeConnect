# from apis.v1 import db
# from apis.v1.models.model import  Model
from datetime import datetime

class ReviewModel():
    """Class to create a Review class object"""

    tablename = 'reviews'

    id = int()
    title = str()
    body = str()
    business = str()
    author_id = str()
    creation_date = str()

    def __init__(self, title, body, business, db_user):
        self.id = int()
        self.title = title
        self.body = body
        self.business = business
        self.author_id = db_user
        self.creation_date = str(datetime.utcnow())

    def __repr__(self):
        return '<Review: {}>'.format(self.title)
