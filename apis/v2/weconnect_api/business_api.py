import datetime

from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, marshal_with

from apis import db
from apis.v2.utils.decorators import authenticate
from apis.v2.utils.validators import validate_business_payload, validate_business_update_payload
from apis.v2.models.user import User
from apis.v2.models.business import BusinessModel
from apis.v2.utils.business_models import api, business_model, post_model, business_parser, update_business_parser


class BusinessList(Resource):
    """Class Representing Businesses Endpoints  """


    @api.doc(responses={
            400: 'Validation Error',
            401: 'Bearer Authentication Error'}, id='get_all_businesses' )
    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.marshal_with(business_model, code=200, description='Displays a list of registered Businesses')
    def get(self, current_user,token):
        """ returns all businesses in the databases """

        businesses = BusinessModel.query.all()

        return businesses, 200


    @api.doc('post biz')
    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(post_model)
    def post(self, current_user,token):
        """ posts a business """

        self.current_user = current_user
        args = business_parser.parse_args()
        new_biz = args
        is_not_valid_input = validate_business_payload(args)

        if is_not_valid_input:
            return is_not_valid_input

        db_user = User.query.filter_by(user_name=self.current_user).first()

        # Adding a business
        new_business = BusinessModel(new_biz['business_name'], new_biz['category'],
                            new_biz['location'], new_biz['profile'],db_user.id)
        db.session.add(new_business)
        db.session.commit()

        # # Return for added business
        # added_business = BusinessModel.query.filter_by(business_name=new_biz['business_name']).first()
        # business_list = added_business.business_as_dict()

        return {'message': 'business added sucessfully'}, 201


class Business(Resource):
    """ This Class handles endpoints for a specific business """

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.marshal_with(business_model, code=200, description='Displays a registered Businesses')
    def get(self, current_user, token, businessId):
        """ returns a specific business """

        find_business = BusinessModel.query.get(businessId)
        if find_business is not None:
            return find_business, 200
        else:
            return {'message': 'business not found'}, 400

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(post_model)
    def put(self, current_user, token, businessId):
        """ updates a specific businesses data """

        business_to_change = BusinessModel.query.get(businessId)
        args = update_business_parser.parse_args()
        biz_to_change =  args
        is_not_valid_input = validate_business_update_payload(args, businessId)

        if is_not_valid_input:
            return is_not_valid_input


        if business_to_change is None:
            return {'message':'There is no Business with ID : {}'.format(businessId)}, 400

        else:

            db_user = User.query.filter_by(user_name=current_user).first()
            if business_to_change.created_by != db_user.id:
                return {'message':'You are not authorised to Change this business'}, 403

                # change business name
            if biz_to_change['business_name'] is not None:

                test_biz = BusinessModel.query.filter_by(business_name=args['business_name']).first()

                if test_biz is not None and test_biz.business_name.lower() != business_to_change.business_name.lower():
                    return {'message': 'business name is already taken'}, 400

                if biz_to_change['business_name'] != business_to_change.business_name:
                    business_to_change.business_name = biz_to_change['business_name']

                # change category
            if biz_to_change['category'] is not None:

                if biz_to_change['category'] != business_to_change.category:
                    business_to_change.category = biz_to_change['category']

                # change location
            if biz_to_change['location'] is not None:

                if biz_to_change['location'] != business_to_change.location:
                    business_to_change.location = biz_to_change['location']

                # change profile
            if biz_to_change['profile'] is not None:

                if biz_to_change['profile'] != business_to_change.profile:
                    business_to_change.profile = biz_to_change['profile']

            db.session.commit()

            return {'result': 'business changed successfully'}, 201


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



"""Business Endpoints"""
api.add_resource(Business, '/<int:businessId>', endpoint="business")
api.add_resource(BusinessList, '', endpoint="businesses")