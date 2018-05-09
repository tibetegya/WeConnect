from flask_restplus import Api, Resource, reqparse, fields, marshal_with
import datetime 

# loacl imports
from apis import db
from apis import api
from apis.v2.models.review import ReviewModel
from apis.v2.models.user import User
from apis.v2.utils import authenticate, validate_review_payload





review_model = api.model('review',{'title': fields.String(),
                'body': fields.String(),
                'author_id': fields.String(),
                'creation_date' : fields.DateTime() })



class Review(Resource):

    @authenticate
    @api.marshal_with(review_model, envelope='reviews')
    def get(self, current_user, businessId):
        
        # get all reviews where the business id is businessId
        biz_reviews = ReviewModel.query.filter_by(business=businessId).all()
        if biz_reviews:
            return biz_reviews , 200
        else:
            return {'message': 'business has no reviews'}, 400


        
    @authenticate
    @api.expect(review_model)
    #@api.marshal_with(review_model, envelope='reviews')
    def post(self, current_user, businessId):
        self.businessId = businessId
        new_review = api.payload

        is_not_valid_input = validate_review_payload(api.payload)
        if is_not_valid_input:
            return is_not_valid_input

        db_user = User.query.filter_by(user_name=current_user).first()
        # Create a new review
        add_review = ReviewModel(new_review['title'], new_review['body'], self.businessId, db_user.id)
        db.session.add(add_review)
        db.session.commit() 


        return {'result':'Review Added'}, 201

