from flask import request, jsonify
from datetime import datetime
from datetime import timezone
from app.extensions import db, jwt

from app.models.user import User
from app.models.token_blocklist import TokenBlocklist
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from app.api import auth_bp

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user account.
    
    Request Body:
    {
      "username": "john_doe",
      "email": "john.doe@example.com",
      "password": "securePassword123",
      "full_name": "John Doe"
    }

    """
    data = request.get_json()
    
    required_fields = ['username', 'email', 'password']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(
        username=data['username'],
        email=data['email'],
        full_name=data.get('full_name', ''),
        balance=0.0
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'message': 'User registered successfully',
        'user': user.to_dict()
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and return a JWT token.
    
    Request Body:
    {
      "username": "",
      "password": ""
    }
    
    """
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify({
        'message': 'Login successful',
        'access_token': access_token
    }), 200
    
@auth_bp.route('/logout', methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify(msg="JWT revoked")

@auth_bp.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    return jsonify(hello="world")

@auth_bp.route('/reset-password', methods=['POST'])
@jwt_required()
def reset_password():
    """
    Reset a user's password. Requires authentication.
    
    Headers:
        Authorization: Bearer <access_token>
    
    Request Body:
    {
      "current_password": "securePassword123",
      "new_password": "newSecurePassword456"
    }
    """
    data = request.get_json()
    user_id = int(get_jwt_identity())
    
    # Validate
    if not data or not data.get('current_password') or not data.get('new_password'):
        return jsonify({'error': 'Missing current or new password'}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if not user.check_password(data['current_password']):
        return jsonify({'error': 'Current password is incorrect'}), 401

    user.set_password(data['new_password'])
    db.session.commit()
    
    return jsonify({'message': 'Password reset successful'}), 200



