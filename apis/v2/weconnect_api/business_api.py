from flask import request, jsonify
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
import datetime 

# local imports  
from apis import db
from apis import api
from apis.v2.utils import authenticate, validate_business_payload, validate_business_update_payload
from apis.v2.models.user import User
from apis.v2.models.business import BusinessModel



'''                                     
=========================================  BUSINESSES API  =========================================
                                        
'''


business_model = api.model('business',{'business_name': fields.String('the business name.'),
                'category': fields.String('the business category.'),
                'location': fields.String('the business\'s location.'),
                'id': fields.Integer(),
                'profile': fields.String('the business logo.'),
                'created_by': fields.String(),
                'creation_date': fields.DateTime()
                })

class BusinessList(Resource):
    """Class Representing Businesses Endpoints  """

    @api.doc(responses={
        400: 'Validation Error',
        401: 'Bearer Authentication Error'
    }, id ='get_all_businesses' )
    @api.header('token', type=str, description ='Authentication token')
    @authenticate
    @api.marshal_with(business_model, code=200 , description='Displays a list of registered Businesses')
    def get(self, current_user):
        
        businesses = BusinessModel.query.all()
        
        return businesses , 200

    api.doc('post biz')
    @api.header('token', type=str, description ='Authentication token')
    @authenticate
    @api.expect(business_model)
    def post(self, current_user):
        self.current_user = current_user
        new_biz = api.payload

        is_not_valid_input = validate_business_payload(api.payload)
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
        
        return {'message': 'business added sucessfully'} , 201


class Business(Resource):

    @authenticate
    @api.marshal_with(business_model, code=200 , description='Displays a registered Businesses')
    def get(self, current_user, businessId):
        find_business = BusinessModel.query.get(businessId)
        if find_business != None:
            return find_business, 200
        else:
            return {'message': 'business not found'} , 400
    
    
    @authenticate
    @api.expect(business_model)
    def put(self, current_user, businessId):
        biz_to_change = api.payload

        is_not_valid_input = validate_business_update_payload(api.payload)
        if is_not_valid_input:
            return is_not_valid_input

        business_to_change = BusinessModel.query.get(businessId)
        if business_to_change == None:
            return {'message':'There is no Business with ID : {}'.format(businessId)}, 400

        db_user = User.query.filter_by(user_name=current_user).first()
        
        if business_to_change.created_by != db_user.id:
            return {'message':'You are not authorised to Change this business'}, 403
        
        
        if business_to_change:
            
            # change business name
            if biz_to_change['business_name'] != business_to_change.business_name:
                business_to_change.business_name = biz_to_change['business_name']
                
            # change category    
            if biz_to_change['category'] != business_to_change.category:
                business_to_change.category = biz_to_change['category']

            # change location
            if biz_to_change['location'] != business_to_change.location:
                business_to_change.location = biz_to_change['location']

            # change profile
            if biz_to_change['profile'] != business_to_change.profile:
                business_to_change.profile = biz_to_change['profile']
            
            # db.session.add(business_to_change)
            db.session.commit()


            return {'result': 'business changed successfully'}, 201
        else:
            return {'message': 'business does not exist'}, 400
    

        
    @authenticate
    def delete(self, current_user, businessId ):
        
        business_to_change = BusinessModel.query.get(businessId)
        db_user = User.query.filter_by(user_name=current_user).first()
        
        if business_to_change == None:
            return {'message':'There is no Business with ID : {}'.format(businessId)}, 400

        if business_to_change.created_by != db_user.id:
            return {'message':'You are not authorised to Change this business'}, 403
            
        check_business = BusinessModel.query.get(businessId)
        if check_business == None:
            return {'message': 'that business does not exist'}, 400
        else:
            
            db.session.delete(check_business)
            db.session.commit()            
        
            return {'result': 'business deleted'}, 201
            
