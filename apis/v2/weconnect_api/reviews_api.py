import datetime

from flask_restplus import Namespace, Api, Resource, fields, marshal_with

from apis import db
from apis.v2.models.review import ReviewModel
from apis.v2.models.user import User
from apis.v2.utils.decorators import authenticate
from apis.v2.utils.validators import validate_review_payload
from apis.v2.utils.review_models import api, review_model, reviews_model, review_parser


class Review(Resource):
    """ this class handles the business reviews endpoints """

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.marshal_with(reviews_model, envelope='reviews')
    def get(self, current_user, token, businessId):
        """ returns a specific business's reviews """

        # get all reviews where the business id is businessId
        biz_reviews = ReviewModel.query.filter_by(business=businessId).all()

        if biz_reviews:
            return biz_reviews , 200
        else:
            return {'message': 'business has no reviews'}, 400

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(review_model)
    #@api.marshal_with(review_model, envelope='reviews')
    def post(self, current_user, token, businessId):
        """ handles posting a review to a specific business """

        self.businessId = businessId
        args = review_parser.parse_args()
        new_review = args

        is_not_valid_input = validate_review_payload(args)
        if is_not_valid_input:
            return is_not_valid_input

        db_user = User.query.filter_by(user_name=current_user).first()
        # Create a new review
        add_review = ReviewModel(new_review['title'], new_review['body'], self.businessId, db_user.id)
        db.session.add(add_review)
        db.session.commit()

        return {'result':'Review Added'}, 201

"""Reviews Endpoints"""
api.add_resource(Review, '/<int:businessId>/reviews', endpoint="reviews")

