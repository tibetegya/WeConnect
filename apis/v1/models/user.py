from apis.v1 import db
from apis.v1.models.model import  Model

class User(Model):
    """ Class that creates a user """


    __tablename__='users'

    id = int()
    email = str()
    user_name = str()
    password_hash = str()
    creation_date = str()

    def __init__(self, user_name, email, password):
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User: {}>'.format(self.user_name)

