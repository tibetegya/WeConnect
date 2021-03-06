from apis import db
from apis.v2.utils.business_models import api, business_model
from flask_restplus import marshal_with

class BusinessModel(db.Model):
    """Class to create a Business class object"""


    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    profile = db.Column(db.String(256))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                onupdate=db.func.current_timestamp())
    creator = db.relationship('User')
    reviews = db.relationship('ReviewModel',order_by='ReviewModel.id',
                                cascade='all, delete-orphan')

    def __init__(self, business_name, category, location, profile, current_user):
        self.business_name = business_name
        self.category = category
        self.location = location
        self.profile = profile
        self.created_by = current_user

    @api.marshal_with(business_model)
    def as_dict(self):
        business_dict = {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        business_dict['creator'] = self.creator.user_name
        return business_dict

    def __repr__(self):
        return '<Business: {}>'.format(self.business_name)
