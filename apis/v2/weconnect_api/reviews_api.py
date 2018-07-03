import datetime

from flask_restplus import Namespace, Api, Resource, fields, marshal_with
from sqlalchemy.exc import IntegrityError

from apis import db
from apis.v2.models.review import ReviewModel
from apis.v2.models.business import BusinessModel
from apis.v2.models.user import User
from apis.v2.utils.decorators import authenticate
from apis.v2.utils.validators import validate_review_payload
from apis.v2.utils.review_models import api, review_model, reviews_model, review_parser


class Review(Resource):
    """ this class handles the business reviews endpoints """

    @api.header('Authorization', type=str, description ='Authentication token')
    def get(self, businessId):
        """ returns a specific business's reviews """

        # get all reviews where the business id is businessId
        reviews_query = ReviewModel.query.filter_by(business=businessId).all()

        if reviews_query:
            reviews = list(r.as_dict() for r in reviews_query if reviews_query)
            return reviews , 200
        else:
            return {'message': 'business has no reviews'}, 200

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    @api.expect(review_model)
    def post(self, current_user, token, businessId):
        """ handles posting a review to a specific business """
        self.businessId = businessId
        args = review_parser.parse_args()
        new_review = args

        is_not_valid_input = validate_review_payload(args)
        if is_not_valid_input:
            return is_not_valid_input

        db_user = User.query.filter_by(user_name=current_user).first()
        business_to_review = BusinessModel.query.get(businessId)
        if business_to_review is None:
            return {'message': 'business does not exist'}, 400
        elif business_to_review.created_by == db_user.id:
            return {'message': 'You can not review your own business'}, 403

        # Create a new review
        new_review = ReviewModel(new_review['title'], new_review['body'], self.businessId, db_user.id)
        db.session.add(new_review)
        db.session.commit()
        review = new_review.as_dict()
        return review, 201

"""Reviews Endpoints"""
api.add_resource(Review, '/<int:businessId>/reviews', endpoint="reviews")

