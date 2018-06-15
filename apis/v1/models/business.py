# from apis.v1 import db
# from apis.v1.models.model import  Model
from datetime import datetime

class BusinessModel():
    """Class to create a Business class object"""

    tablename = 'businesses'

    id = int()
    business_name = str()
    category = str()
    location = str()
    profile = str()
    created_by = str()
    creation_date = str()

    def __init__(self, business_name, category, location, profile, current_user):
        self.id = int()
        self.business_name = business_name
        self.category = category
        self.location = location
        self.profile = profile
        self.created_by = current_user
        self.creation_date = str(datetime.utcnow())

    def __repr__(self):
        return '<Business: {}>'.format(self.business_name)
