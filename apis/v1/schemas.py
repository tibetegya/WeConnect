from models.blacklist import Blacklist
# from apis.v1.models.business import BusinessModel
# from apis.v1.models.review import ReviewModel
# from apis.v1.models.user import User




class Database:
    """ class that defines how a database behaves"""

    database = dict()
    def __init__(self):
        pass

    def commit(self, obj):
        self.obj = obj
        if isinstance(self.obj, Blacklist):
            blacklist.append(self.obj)

        elif isinstance(self.obj, BusinessModel):
            businesses.append(self.obj)

        elif isinstance(self.obj, ReviewModel):
            reviews.append(self.obj)

        elif isinstance(self.obj, User):
            users.append(self.obj)


    def delete(self, obj):
        pass


    def update(self, obj):
        pass
    @classmethod
    def drop_all(self, obj):
        pass

    @classmethod
    def create_all(self, *args):

        for clas in args:
            self.table_key = clas.tablename
            self.database[self.table_key] = list()








# class Model(object):

# def __init__(self):
#     pass

# @classmethod
# def filter_by(cls, obj):
#     pass

# @classmethod
# def get(cls, int):
#     pass

# @classmethod
# def get_all(cls):
#     pass
