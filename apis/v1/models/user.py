# from apis.v1 import db
# from apis.v1.models.model import  Model
from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
from datetime import datetime


class User():
    """ Class that creates a user """

    tablename = 'users'

    id = int()
    email = str()
    user_name = str()
    password_hash = str()
    creation_date = str()

    def __init__(self, user_name, email, password):
        self.id = int()
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)
        self.creation_date = str(datetime.utcnow())

    def __repr__(self):
        return '<User: {}>'.format(self.user_name)

