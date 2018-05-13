import datetime

from flask_restplus import Api, Resource, reqparse, fields, marshal_with

from apis.v1 import ns_1 as api


businesses = []

business_model = api.model('business',{'business_name': fields.String('the business name.'),
                # 'id': fields.Integer(1),
                'location': fields.String('the business\'s location.'),
                'category': fields.String('the business category.'),
                'profile': fields.String('the business logo.')
                # 'creation_date': fields.Date(),
                # 'business_owner': fields.String('user that created')
                })


class BusinessList(Resource):
    """ Handles the business endpoints for all businesses """


    @api.doc(responses={400: 'Validation Error',
                        401: 'Bearer Authentication Error'},
                        id ='get_all_businesses' )
    #@api.header('token', type=str, description ='Authentication token')
    @api.marshal_with(business_model, code=200,
                        description='Displays a list of registered Businesses')
    # @authenticate
    def get(self):
        """ Returns all businesses in the database """

        return businesses , 200


    #@authenticate
    @api.expect(business_model)
    def post(self):
        """ Method for Posting a Business """

        new_biz = api.payload
        new_biz['id'] = len(businesses)+1
        businesses.append(new_biz)
        return businesses[-1] , 201



class Business(Resource):
    """ Handles Endpoints for a specific Business """


    def get(self, businessId):
        """ Method for returning a specific Business """

        return businesses[businessId-1], 200


    @api.expect(business_model)
    def put(self, businessId):
        """ Method for Updating a Specific business """

        biz_to_change = api.payload
        found = False
        if type(businessId) == int :
            if businessId > len(businesses):
                return {'message': 'bad request Yo !'}, 400
            else:
                for biz in businesses:
                    if biz['id'] == biz_to_change['id']:
                        found = True
                        businesses[businessId-1] = biz_to_change
                        return {'result': 'business changed successfully'}, 201
        if found == False :
            return {'result': 'business does not exist'}, 404


    def delete(self, businessId ):
        """ Method for deleting a Specific business """

        biz_to_delete = api.payload
        if type(businessId) != int :
            return {'message': 'business id must be an integer'}, 400
        else:
            if businessId > len(businesses):
                return {'message': 'bad request Yo!'}, 400
            else:
                for biz in businesses:
                    if biz['id'] ==  biz_to_delete['id']:

                            del businesses[businessId-1]
                            return {'result': 'business deleted'}, 201
                else:
                    return {'message': 'We Don\' t know that business Yo!'}, 404

