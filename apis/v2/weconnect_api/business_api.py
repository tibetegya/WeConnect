from flask import request
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
import datetime 

# local imports  
from apis import db
from apis import api
from apis.v2.weconnect_api.users_api import authenticate
from apis.v2.models.business import BusinessModel



'''                                     
=========================================  BUSINESSES API  =========================================
                                        
'''


business_model = api.model('business',{'business_name': fields.String('the business name.'),
                'category': fields.String('the business category.'),
                'location': fields.String('the business\'s location.'),
                'profile': fields.String('the business logo.')
                })

class BusinessList(Resource):

    @api.doc(responses={
        400: 'Validation Error',
        401: 'Bearer Authentication Error'
    }, id ='get_all_businesses' )
    @api.header('token', type=str, description ='Authentication token')
    #@authenticate
    @api.marshal_with(business_model, code=200 , description='Displays a list of registered Businesses')
    def get(self):
        # businesses = BusinessModel.business_as_dict()
        businesses = BusinessModel.query.all()
        businesses_returned = businesses.business_as_dict
        return businesses_returned , 200

    api.doc('post biz')
    #@authenticate
    @api.expect(business_model)
    def post(self):
        new_biz = api.payload


        # Adding a business
        new_business = BusinessModel(new_biz['business_name'], new_biz['category'],
                            new_biz['location'], new_biz['profile'])
        db.session.add(new_business)
        db.session.commit()

        # Return for added business
        added_business = BusinessModel.query.filter_by(business_name=new_biz['business_name']).first()
        return added_business.business_as_dict() , 201


class Business(Resource):

    def get(self, businessId):
        find_business = BusinessModel.query.get(businessId)
        if find_business != None:
            return find_business.business_as_dict(), 200
        else:
            return {'message': 'business not found'} , 404
    
    @api.expect(business_model)
    def put(self, businessId):
        biz_to_change = api.payload
        business_to_change = BusinessModel.query.get(businessId)
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
            
            db.session.add(business_to_change)
            db.session.commit


            return {'result': 'business changed successfully'}, 201
        else:
            return {'message': 'business does not exist'}, 404
    

        
    
    def delete(self, businessId ):
        if type(businessId) != int :
            return {'message': 'business id must be an integer'}, 400
        else:
            check_business = BusinessModel.query.get(businessId)
            if check_business == None:
                return {'message': 'that business does not exist'}, 400
            else:
                
                db.session.delete(check_business)
                db.session.commit()            
            
                return {'result': 'business deleted'}, 201
                
