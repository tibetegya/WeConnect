from flask import Blueprint, request, Response, jsonify
from weconnect.controllers.auth import AuthControllers

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v3/auth')

@auth_bp.route('/users', methods=['GET'])
def get_users():
  response = AuthControllers.get_many()
  return jsonify(response), 201

@auth_bp.route('/register', methods=['POST'])
def register_user():
  return 'page auth'

@auth_bp.route('/login', methods=['POST'])
def login_user():
  return 'page auth'

@auth_bp.route('/logout', methods=['GET'])
def logout_user():
  return 'page auth'

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
  return 'page auth'