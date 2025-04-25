from flask import request, jsonify
from app.extensions import db
from app.models.user import User
from app.models.transaction import Transaction
from flask_jwt_extended import jwt_required, get_jwt
from app.api import staff_bp

@staff_bp.route('/transactions', methods=['POST'])
@jwt_required()
def create_staff_transaction():
    data = request.get_json()
    # identity = get_jwt_identity()
    
    claims = get_jwt()
    is_staff = claims.get('is_staff', False)

    if not is_staff:
        return jsonify({'error': 'Unauthorized. Staff access required'}), 403
    
    required_fields = ['user_id', 'reference', 'amount']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    amount = float(data['amount'])
    if user.balance + amount < 0:
        return jsonify({'error': 'Transaction would result in negative balance'}), 400
    
    previous_balance = user.balance
    user.balance += amount
    
    transaction = Transaction(
        reference=data['reference'],
        user=user.id,
        previous_balance=previous_balance,
        amount=amount,
        balance=user.balance
    )
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({
        'message': 'Staff transaction created successfully',
        'transaction': transaction.to_dict(),
        'user_balance': user.balance
    }), 201
    
    
    
