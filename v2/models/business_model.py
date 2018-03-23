from sqlalchemy import ForeignKey
from app import db

class Business(db.Model):
    """This class represents the business table."""

    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    user = db.relationship(User, backref='business')

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Business.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Business: {}>".format(self.name)