from apis import db
from apis.v2.utils.review_models import api, reviews_model
from flask_restplus import marshal_with


class ReviewModel(db.Model):
    """Class to create a Review class object"""


    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(256), nullable=False)
    business = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())
    author = db.relationship('User')

    def __init__(self, title, body, business, db_user):
        self.title = title
        self.body = body
        self.business = business
        self.author_id = db_user

    @api.marshal_with(reviews_model, envelope='reviews')
    def as_dict(self):
        business_dict = {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        business_dict['author'] = self.author.user_name
        return business_dict

    def __repr__(self):
        return '<Review: {}>'.format(self.title)
