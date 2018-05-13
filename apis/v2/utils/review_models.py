from flask_restplus import Namespace, Api, Resource, reqparse, fields

api = Namespace('reviews', path='/businesses', description='Reviews endpoints')



reviews_model = api.model('review',{'title': fields.String(),
                'body': fields.String(),
                'author_id': fields.String(),
                'creation_date' : fields.DateTime() })

review_model = api.model('review',{'title': fields.String(),
                                    'body': fields.String()})

review_parser = reqparse.RequestParser()
review_parser.add_argument('title', type=str, required=True, help='user name should be a string', location='json')
review_parser.add_argument('body', type=str, required=True, help='user name should be a string', location='json')