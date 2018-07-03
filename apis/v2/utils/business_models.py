from flask_restplus import Namespace, Api, Resource, reqparse, fields


api = Namespace('businesses', description='Businesses endpoints')


business_model = api.model('business', {'business_name': fields.String(),
                            'category': fields.String(),
                            'location': fields.String(),
                            'id': fields.Integer(),
                            'profile': fields.String(),
                            'creator': fields.String(),
                            'creation_date': fields.String()})

post_model = api.model('business post', {'business_name': fields.String('business1'),
                            'category': fields.String('category1'),
                            'location': fields.String('example location'),
                            'profile': fields.String('the business profile or description')})

business_parser = reqparse.RequestParser()
business_parser.add_argument('business_name', required=True, type=str, help='user name should be a string', location='json')
business_parser.add_argument('category', required=True, type=str, help='user name should be a string', location='json')
business_parser.add_argument('location', required=True, type=str, help='user name should be a string', location='json')
business_parser.add_argument('profile', required=True, type=str, help='user name should be a string', location='json')

update_business_parser = reqparse.RequestParser()
update_business_parser.add_argument('business_name', type=str, help='user name should be a string', location='json')
update_business_parser.add_argument('category',type=str, help='user name should be a string', location='json')
update_business_parser.add_argument('location', type=str, help='user name should be a string', location='json')
update_business_parser.add_argument('profile', type=str, help='user name should be a string', location='json')

search_parser = reqparse.RequestParser()
search_parser.add_argument('limit', type=int, trim=True,  default=8, location='args')
search_parser.add_argument('location', type=str, trim=True, location='args')
search_parser.add_argument('category', type=str, trim=True, location='args')
search_parser.add_argument('creator', type=str, trim=True, location='args')
search_parser.add_argument('q', type=str, trim=True, location='args')
search_parser.add_argument('page', type=int, trim=True,  default=1, location='args')