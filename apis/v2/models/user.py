from werkzeug.security import generate_password_hash

from apis import db
from apis.v2.models.business import BusinessModel


class User(db.Model):
    """ Class that creates a user """


    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

    businesses = db.relationship('BusinessModel', order_by='BusinessModel.id',
                                    cascade='all, delete-orphan')

    def __init__(self, user_name, email, password):
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User: {}>'.format(self.user_name)


