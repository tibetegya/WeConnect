from apis.v1.models.blacklist import Blacklist
from apis.v1.models.business import BusinessModel
from apis.v1.models.review import ReviewModel
from apis.v1.models.user import User




class Database:
    """ class that defines how a database behaves"""

    database = dict()
    max_ids = dict()
    def __init__(self):
        self.max_ids = dict()

    def commit(self, obj):
        self.obj = obj
        self.assign_id(obj)
        self.database[self.obj.tablename].append(self.obj.__dict__)

    def assign_id(self, obj):
        max_id = self.max_ids[obj.tablename]
        table_length = len(self.database[obj.tablename])
        if max_id > table_length:
            obj.id = max_id + 1
            self.max_ids[obj.tablename] += 1
        elif max_id <= table_length:
            obj.id = table_length + 1
            self.max_ids[obj.tablename] += 1



    def get_all(self, clas):
        table = self.database[clas.tablename]
        return table



    def get(self, clas, num):
        table = self.database[clas.tablename]
        found = False

        for item in table:
            if item['id'] == num:
                found = True
                return item
        if not found:
            return None

    def delete(self, clas, dic):

        table = self.database[clas.tablename]
        for item in table:
            if item['id'] == dic['id']:
                it = table.index(item)
                del table[it]



    def update(self, clas, obj):
        update_id = obj['id']
        table = self.database[clas.tablename]
        for item in table:
            if item['id'] == update_id:
                location = table.index(item)
                table[location] = obj


    def drop_all(self):
        self.database.clear()


    def create_all(self, *args):

        for clas in args:
            self.table_key = clas.tablename
            self.database[self.table_key] = list()
            self.max_ids[clas.tablename] = int()

    def filter_by(self, obj, param, val):
        table = self.database[obj.tablename]
        found = False

        for item in table:
            if item[param] == val:
                found = True
                return item
        if not found:
            return None


db = Database()
db.create_all(Blacklist, BusinessModel, ReviewModel, User)
