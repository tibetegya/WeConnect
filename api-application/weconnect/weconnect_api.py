"""
    :weconnect_api:
    ~~~~~
    
    A module that contains the endpoints for the WeConnect restful API.

"""

from flask import Flask,jsonify, abort, make_response,render_template, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal
from weconnect import api, app

@app.route('/')
def index():
    return render_template('index.html')

'''
USERS API

'''
users = [
            {
            'id': 1,
            'user_name': 'george',
            'email': 'george@andela.com',
            'password': 'fgjsjdncnnv',
            'profile': 'image.png'
                },
                {
            'id': 2,
            'user_name': 'joan',
            'email': 'joan@andela.com',
            'password': 'fgjsjdncnnv',
            'profile': 'image.png'
                },
                {
            'id': 3,
            'user_name': 'adam',
            'email': 'adam@andela.com',
            'password': 'fgjsjdncnnv',
            'profile': 'image.png'
                },
                {
            'id': 4,
            'user_name': 'kim',
            'email': 'kim@andela.com',
            'password': 'fgjsjdncnnv',
            'profile': 'image.png'
                },
                {
            'id': 5,
            'user_name': 'john',
            'email': 'john@andela.com',
            'password': 'fgjsjdncnnv',
            'profile': 'image.png'
                },
        ]

user_fields = {
    'user_name': fields.String,
    'email': fields.String,
    'password': fields.String,
    'profile': fields.String
}

class UserAPI(Resource):


    def __init__(self):
        self.weparser = reqparse.RequestParser()
        self.weparser.add_argument('id', type=int, required=True, help='No User Name provided', location='json')
        self.weparser.add_argument('user_name', type=str, required=True, help='No User Name provided', location='json')
        self.weparser.add_argument('email', type=str, required=True, help='No User Name provided', location='json')
        self.weparser.add_argument('password', type=str, required=True, help='No User Name provided', location='json')
        self.weparser.add_argument('profile', type=str, help='No User Name provided', location='json')
        super(UserAPI, self).__init__()

    def post(self):
        args = self.weparser.parse_args()
        user={
            'email': args['email'],
            'user_name': args['user_name'],
            'password': args['password'],
            'profile': args['profile']
        }
        users[len(users)] = user
        return users[len(users)-1] ,201


class LoginAPI(Resource):
    def __init__(self):
        self.weparser = reqparse.RequestParser()
        self.weparser.add_argument('email', type=str, required=True, help='No User Name provided', location='json')
        self.weparser.add_argument('password', type=str, required=True, help='No User Name provided', location='json')
        super(LoginAPI, self).__init__()


    def post(self):
        args = self.weparser.parse_args()
        user={
            'email': args['email'],
            'password': args['password']
        }
        
        for person in users:
            if person['email']== user['email'] and person['password'] == user['password']:
                return {'authenticated': True } , 201


'''
BUSINESS API

'''

businesses = {
    'business1':{
        'id': 1,
        'name': 'Business 1',
        'location': 'kampala',
        'category': 'category2',
        'profile': 'picture.png',
        'creation_date': '21 Febuary 2018',
        'business_owner': 'george'        
        },
    'business2':{
        'id': 2,
        'name': 'Business 2',
        'location': 'mukono',
        'category': 'category2',
        'profile': 'picture.png',
        'creation_date': '21 Febuary 2018',
        'business_owner': 'george'        
        },
}

parser = reqparse.RequestParser()
parser.add_argument('business')
args = parser.parse_args()
biz = {
                    'id': args['id'] ,
                    'name': args['name'],
                    'location': args['location'],
                    'category': args['category'],
                    'profile': args['profile'],
                    'creation_date': args['date'],
                    'business_owner': args['business_owner']        
                    }


class Business(Resource):
    def get(self, business_id):
        return businesses[business_id]
        
    def delete(self, business_id):
        del businesses[business_id]
        return '', 204
    def put(self, business_id):
        args = parser.parse_args()
        business = biz
        businesses[business_id] = business
        return business, 201

class BusinessList(Resource):
    def get(self):
        return businesses

    def post(self):
        args = parser.parse_args()
        business_id = int(max(businesses.keys()).lstrip('business')) + 1
        business_id = 'business%i' % business_id
        businesses[business_id] = biz
        return businesses[business_id], 201

'''
BUSINESS API

'''


reviews = [
    {
        'id': 1,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 1,
        'author': 'George',
        'creation_date': '21 Febuary 2018'
        },
    {
        'id': 2,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 4,
        'author': 'Grace',
        'creation_date': '21 Febuary 2018'        
        },
    {
        'id': 3,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 1,
        'author': 'Brian',
        'creation_date': '21 Febuary 2018'
        },
    {
        'id': 4,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 2,
        'author': 'Richard',
        'creation_date': '21 Febuary 2018'        
        }
]




parser = reqparse.RequestParser()
parser.add_argument('review')

class Review(Resource):

    def find_reviews(self, biz_id):
        business_reviews = []

        for review in reviews:
            if review['business'] == biz_id:
                business_reviews.append(review)
        
        return business_reviews

    def get(self, business_id):
        biz_reviews = self.find_reviews(business_id)
        revus = {}
        for i in range(len(biz_reviews)):
            revus[str(i)] = biz_reviews[i] 

        return revus
    def post(self, business_id):
        args = parser.parse_args()
        rev_dict = {
            'id': args['id'],
            'title': args['title'],
            'body': args['body'],
            'business': args['business'],
            'author': args['author'],
            'creation_date': args['creation_date']
        } 
        reviews.append(rev_dict)
        return reviews[len(reviews)], 201




api.add_resource(UserAPI, '/api/v2/auth/register', endpoint = 'Register')
api.add_resource(LoginAPI, '/api/v2/auth/login', endpoint = 'login')

api.add_resource(BusinessList, '/api/v2/businesses')
api.add_resource(Business, '/api/v2/businesses/<business_id>')

api.add_resource(Review, '/api/v2/businesses/<int:business_id>/reviews')