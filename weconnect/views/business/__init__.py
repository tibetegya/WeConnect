from flask import Blueprint, request

business_bp = Blueprint('business', __name__, url_prefix='/api/v3/businesses')

@business_bp.route('/', methods=['GET', 'POST'])
def index():
  return 'all businesses'

@business_bp.route('/<int:businessId>', methods=['GET', 'POST'])
def single_business(businessId):
  if (request.method == 'GET'):
    return 'one business page'
  elif (request.method == 'POST'):
    return 'one business page with id {}'.format(businessId)

@business_bp.route('/<int:businessId>/reviews', methods=['GET', 'POST'])
def business_reviews(businessId):
  return 'business page'