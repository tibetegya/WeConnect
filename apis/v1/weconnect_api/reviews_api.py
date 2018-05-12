import datetime

from flask_restplus import Api, Resource, reqparse, fields, marshal_with

from apis import api


review_model = api.model('review',{'title': fields.String('review title.'),
                # 'id': fields.Integer(1),
                'body': fields.String('body'),
                # 'business': fields.Integer(),
                'author': fields.String('user that created'),
                # 'creation_date': fields.Date()
                 })

reviews = []



class Review(Resource):
    """ Class for handling reviews endpoints """


    @api.marshal_with(review_model, envelope='reviews')
    def get(self, businessId):
        """ method for returning reviews for a specific business """

        biz_reviews = []

        for rev in reviews:
            if rev['business'] == businessId:
                biz_reviews.append(rev)

        return biz_reviews , 200


    @api.expect(review_model)
    # @api.marshal_with(review_model, envelope='reviews')
    def post(self, businessId):
        """ method that handles posting a reviews for a specific business """

        new_review = api.payload
        new_review['id'] = len(reviews)+1
        new_review['business'] = businessId
        new_review['creation_date'] = str(datetime.datetime.utcnow())

        reviews.append(new_review)
        return {'result':'Review Added'}, 201
