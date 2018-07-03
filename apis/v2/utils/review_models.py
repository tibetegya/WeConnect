from flask_restplus import Namespace, Api, Resource, reqparse, fields

api = Namespace('reviews', path='/businesses', description='Reviews endpoints')



reviews_model = api.model('review',{'title': fields.String(),
                'id': fields.Integer(),
                'body': fields.String(),
                'author': fields.String(),
                'creation_date' : fields.String() })

review_model = api.model('review',{'title': fields.String(),
                                    'body': fields.String()})

review_parser = reqparse.RequestParser()
review_parser.add_argument('title', type=str, required=True, help='user name should be a string', location='json')
review_parser.add_argument('body', type=str, required=True, help='user name should be a string', location='json')