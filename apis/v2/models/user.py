from werkzeug.security import generate_password_hash

# local imports
from apis import db

class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_date = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    # businesses = db.relationship(
    #     'Business', order_by='Business.id', cascade='all, delete-orphan')

    def __init__(self, user_name, email, password):
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def user_as_dict(self):
        """Represent the user as a dict"""

        return {u.name: getattr(self, u.name) for u in self.__table__.columns}
