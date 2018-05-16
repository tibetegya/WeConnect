from datetime import datetime
# from apis.v1 import db
# from apis.v1.models.model import  Model

class Blacklist():
    """Class for blacklisted tokens"""

    tablename = 'blacklists'

    id = int()
    token = str()
    creation_date = str()

    def __init__(self, token):
        self.id = int()
        self.token = token
        self.creation_date = str(datetime.utcnow())

    def __repr__(self):
        return '<Token: {}>'.format(self.token)

