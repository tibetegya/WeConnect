import datetime

from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, marshal_with
from sqlalchemy.exc import IntegrityError

from apis import db
from apis.v2.utils.decorators import authenticate
from apis.v2.utils.validators import validate_business_payload, validate_business_update_payload, validate_search_payload
from apis.v2.models.user import User
from apis.v2.models.business import BusinessModel
from apis.v2.utils.business_models import api, business_model, post_model
from apis.v2.utils.business_models import business_parser, update_business_parser, search_parser


SEARCH_KEYS = ['location', 'category']


class BusinessList(Resource):
    """Class Representing Businesses Endpoints  """


    @api.doc(responses={
            400: 'Validation Error',
            401: 'Bearer Authentication Error'}, id='get_all_businesses' )
    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    def get(self, current_user,token):
        """ returns all businesses in the databases """
        args = search_parser.parse_args()
        is_not_valid_input = validate_search_payload(args)

        if is_not_valid_input:
            return is_not_valid_input

        if args['q'] is not None:
            businesses_query = (BusinessModel.query.filter(
                            BusinessModel.business_name.ilike('%'+args['q']+'%')))
        else:
            businesses_query = BusinessModel.query

        if args['location'] is not None:
            businesses_query = businesses_query.filter_by(location=args['location'].strip(' '))
        if args['category'] is not None:
            businesses_query = businesses_query.filter_by(category=args['category'].strip(' '))

        businesses_paginated = businesses_query.paginate(page=args['page'],
                                                    per_page=args['limit'], error_out=False)
        businesses = businesses_paginated.items
        businesses = to_list(businesses)

        next_page = businesses_paginated.next_num if businesses_paginated.has_next else None
        prev_page = businesses_paginated.prev_num if businesses_paginated.has_prev else None
        businesses_response = {"businesses": businesses,
                                "next_page": next_page, "prev_page": prev_page}

        return businesses_response, 200


    @api.doc('post biz')
    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(post_model)
    def post(self, current_user,token):
        """ posts a business """

        try:
            self.current_user = current_user
            args = business_parser.parse_args()
            new_biz = args
            is_not_valid_input = validate_business_payload(args)

            if is_not_valid_input:
                return is_not_valid_input

            db_user = User.query.filter_by(user_name=self.current_user).first()

            # Adding a business
            new_business = BusinessModel(new_biz['business_name'].strip(' ').lower(), new_biz['category'].strip(' '),
                                new_biz['location'].strip(' '), new_biz['profile'],db_user.id)
            db.session.add(new_business)
            db.session.commit()
            business = new_business.as_dict()

            return business, 201
        except IntegrityError:
            return {'message':'Business With this name already exists'}, 400

class Business(Resource):
    """ This Class handles endpoints for a specific business """

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    def get(self, current_user, token, businessId):
        """ returns a specific business """

        found_business = BusinessModel.query.get(businessId)
        if found_business is not None:
            return found_business.as_dict(), 200
        else:
            return {'message': 'business not found'}, 400

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(post_model)
    def put(self, current_user, token, businessId):
        """ updates a specific businesses data """

        business_to_change = BusinessModel.query.get(businessId)
        args = update_business_parser.parse_args()
        business_inputs =  args
        is_not_valid_input = validate_business_update_payload(args, businessId)

        if is_not_valid_input:
            return is_not_valid_input


        try:

            if business_to_change is None:
                return {'message':'There is no Business with ID : {}'.format(businessId)}, 400

            else:

                db_user = User.query.filter_by(user_name=current_user).first()
                if business_to_change.created_by != db_user.id:
                    return {'message':'You are not authorised to Change this business'}, 403

                    # change business name
                if business_inputs['business_name'] is not None and business_inputs['business_name'].strip(' ') != '':

                    test_biz = BusinessModel.query.filter_by(business_name=business_inputs['business_name'].strip(' ').lower()).first()

                    if test_biz is not None and test_biz.business_name.lower() != business_to_change.business_name.lower():
                        return {'message': 'business name is already taken'}, 400

                    if business_inputs['business_name'].strip(' ') != business_to_change.business_name:
                        business_to_change.business_name = business_inputs['business_name'].lower()

                    # change category
                if business_inputs['category'] is not None and business_inputs['category'].strip(' ') != '':

                    if business_inputs['category'] != business_to_change.category:
                        business_to_change.category = business_inputs['category'].strip(' ')

                    # change location
                if business_inputs['location'] is not None and business_inputs['location'].strip(' ') != '':

                    if business_inputs['location'] != business_to_change.location:
                        business_to_change.location = business_inputs['location'].strip(' ')

                    # change profile
                if business_inputs['profile'] is not None and business_inputs['profile'].strip(' ') != '':

                    if business_inputs['profile'] != business_to_change.profile:
                        business_to_change.profile = business_inputs['profile'].strip(' ')
            db.session.commit()
            return {'result': 'business changed successfully'}, 201
        except IntegrityError:
            return {'Business With this name already exists'}, 400



    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    def delete(self, current_user, token, businessId):
        """ deletes a specific businesses """

        business_to_change = BusinessModel.query.get(businessId)
        db_user = User.query.filter_by(user_name=current_user).first()

        if business_to_change is None:
            return {'message':'There is no Business with ID : {}'.format(businessId)}, 400

        else:
            if business_to_change.created_by != db_user.id:
                return {'message':'You are not authorised to Change this business'}, 403

            else:
                db.session.delete(business_to_change)
                db.session.commit()
                return {'message': 'business deleted'}, 201



@api.marshal_with(business_model)
def to_list(businesses_query):
    return list(b.as_dict() for b in businesses_query if businesses_query)

"""Business Endpoints"""
api.add_resource(Business, '/<int:businessId>', endpoint="business")
api.add_resource(BusinessList, '', endpoint="businesses")