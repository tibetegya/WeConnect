from flask import jsonify
from app import app



@app.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    return {'hello': 'world'}

@app.route('/api/v1/auth/login', methods=['POST'])
def user_login():
    return {'hello': 'world'}


@app.route('/api/v1/auth/logout', methods=['POST'])
def user_logout():
    return {'hello': 'world'}


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def password_reset():
    return {'hello': 'world'}


@app.route('/api/v1/businesses', methods=['POST'])
def business_register():
    return {'hello': 'world'}


@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
def business_update():
    return {'hello': 'world'}


@app.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
def business_delete():
    return {'hello': 'world'}   