import datetime

from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, marshal_with

from apis.v1.schemas import db, User, BusinessModel
from apis.v1.utils.decorators import authenticate
from apis.v1.utils.validators import validate_business_payload, validate_business_update_payload
# from apis.v1.models.user import User
# from apis.v1.models.business import BusinessModel
from apis.v1.utils.business_models import api, business_model, post_model, business_parser, update_business_parser

PAYLOAD_KEYS = ['business_name', 'category', 'location', 'profile']


class BusinessList(Resource):
    """Class Representing Businesses Endpoints  """

    @api.doc(responses={
        400: 'Validation Error',
        401: 'Bearer Authentication Error'}, id='get_all_businesses')
    @api.header('Authorization', type=str, description='Authentication token')
    @authenticate
    @api.marshal_with(business_model, code=200,
                      description='Displays a list of registered Businesses')
    def get(self, current_user, token):
        """ returns all businesses in the databases """

        businesses = db.get_all(BusinessModel)

        return businesses, 200

    @api.doc('post business')
    @api.header('Authorization', type=str, description='Authentication token')
    @authenticate
    @api.expect(post_model)
    def post(self, current_user, token):
        """ posts a business """

        self.current_user = current_user
        args = business_parser.parse_args()
        new_business = args
        is_not_valid_input = validate_business_payload(args)

        if is_not_valid_input:
            return is_not_valid_input

        db_user = db.filter_by(User, 'user_name', self.current_user)

        # Adding a business
        added_business = BusinessModel(new_business['business_name'], new_business['category'],
                                       new_business['location'], new_business['profile'], db_user['id'])
        db.commit(added_business)

        return {'message': 'business added sucessfully'}, 201


class Business(Resource):
    """ This Class handles endpoints for a specific business """

    @api.header('Authorization', type=str, description='Authentication token')
    @authenticate
    @api.marshal_with(business_model, code=200,
                      description='Displays a registered Businesses')
    def get(self, current_user, token, businessId):
        """ returns a specific business """

        found_business = db.get(BusinessModel, businessId)
        if found_business is not None:
            return found_business, 200
        else:
            return {'message': 'business not found'}, 400

    @api.header('Authorization', type=str, description='Authentication token')
    @authenticate
    @api.expect(post_model)
    def put(self, current_user, token, businessId):
        """ updates a specific businesses data """

        business_to_change = db.get(BusinessModel, businessId)
        args = update_business_parser.parse_args()
        busines_payload = args
        is_not_valid_input = validate_business_update_payload(args, businessId)

        if is_not_valid_input:
            return is_not_valid_input

        if business_to_change is None:
            return {'message': 'There is no Business with ID : {}'.format(
                businessId)}, 400

        else:

            db_user = db.filter_by(User, 'user_name', current_user)
            if business_to_change['created_by'] != db_user['id']:
                return {
                    'message': 'You are not authorised to Change this business'}, 403

                # change business name
            for key in PAYLOAD_KEYS:
                if key == 'business_name':
                    test_business = db.filter_by(
                        BusinessModel, 'business_name', args['business_name'])

                    if test_business is not None and test_business['business_name'].lower(
                    ) != business_to_change['business_name'].lower():
                        return {'message': 'business name is already taken'}, 400

                if busines_payload[key] is not None:

                    if busines_payload[key] != business_to_change[key]:
                        business_to_change[key] = busines_payload[key]

            # if busines_payload['business_name'] is not None:

            #     test_business = db.filter_by(BusinessModel,'business_name', args['business_name'])

            #     if test_business is not None and test_business['business_name'].lower() != business_to_change['business_name'].lower():
            #         return {'message': 'business name is already taken'}, 400

            #     if busines_payload['business_name'] != business_to_change['business_name']:
            #         business_to_change['business_name'] = busines_payload['business_name']

            #     # change category
            # if busines_payload['category'] is not None:

            #     if busines_payload['category'] != business_to_change['category']:
            #         business_to_change['category'] = busines_payload['category']

            #     # change location
            # if busines_payload['location'] is not None:

            #     if busines_payload['location'] != business_to_change['location']:
            #         business_to_change['location'] = busines_payload['location']

            #     # change profile
            # if busines_payload['profile'] is not None:

            #     if busines_payload['profile'] != business_to_change['profile']:
            #         business_to_change['profile'] = busines_payload['profile']

            db.update(BusinessModel, business_to_change)

            return {'result': 'business changed successfully'}, 201

    @api.header('Authorization', type=str, description='Authentication token')
    @authenticate
    def delete(self, current_user, token, businessId):
        """ deletes a specific businesses """

        business_to_change = db.get(BusinessModel, businessId)
        db_user = db.filter_by(User, 'user_name', current_user)

        if business_to_change is None:
            return {'message': 'There is no Business with ID : {}'.format(
                businessId)}, 400

        else:
            if business_to_change['created_by'] != db_user['id']:
                return {
                    'message': 'You are not authorised to Change this business'}, 403

            else:
                db.delete(BusinessModel, business_to_change)
                return {'message': 'business deleted'}, 201


"""Business Endpoints"""
api.add_resource(Business, '/<int:businessId>', endpoint="business")
api.add_resource(BusinessList, '', endpoint="businesses")
