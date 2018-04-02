from flask_restplus import Api, Resource, reqparse, fields, marshal_with
import datetime 

# loacl imports
from apis.v2 import api, db
from apis.v2.models.review import ReviewModel






review_model = api.model('review',{'title': fields.String('review title.'),
                'body': fields.String('body'),
                'author': fields.String('user that created')
                 })


# reviews = []
class Review(Resource):

    @api.marshal_with(review_model, envelope='reviews')
    def get(self, businessId):
        
        # get all reviews where the business id is businessId
        biz_reviews = ReviewModel.query.filter_by(business=businessId).all()
        if biz_reviews:
            return biz_reviews.review_as_dict() , 200
        else:
            return {'message': 'business has no reviews'}, 404


        

    @api.expect(review_model)
    # @api.marshal_with(review_model, envelope='reviews')
    def post(self, businessId):
        self.businessId = businessId
        new_review = api.payload

        # Create a new review
        add_review = ReviewModel(new_review['title'], new_review['body'], self.businessId)
        db.session.add(add_review)
        db.session.commit() 


        return {'result':'Review Added'}, 201

