from app import db

class Business(db.Model):
    """This class represents the business table."""

    __tablename__ = 'businesses'