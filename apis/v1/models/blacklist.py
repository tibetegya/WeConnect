from datetime import datetime
# from apis.v1 import db
# from apis.v1.models.model import  Model

class Blacklist():
    """Class for blacklisted tokens"""

    tablename = 'blacklists'

    id = int()
    token = str()
    creation_date = datetime

    def __init__(self, token):
        self.token = token
        self.creation_date = datetime.utcnow()

    def __repr__(self):
        return '<Token: {}>'.format(self.token)

