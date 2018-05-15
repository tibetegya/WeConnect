# from apis.v1 import db
# from apis.v1.models.model import  Model


class BusinessModel(Model):
    """Class to create a Business class object"""

    id = int()
    business_name = str()
    category = str()
    location = str()
    profile = str()
    created_by = str()
    creation_date = str()

    def __init__(self, business_name, category, location, profile, current_user):
        self.business_name = business_name
        self.category = category
        self.location = location
        self.profile = profile
        self.created_by = current_user

    def __repr__(self):
        return '<Business: {}>'.format(self.business_name)
