from flask import request, jsonify
from app.extensions import db
from app.models.user import User
from app.models.transaction import Transaction
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api import transaction_bp

@transaction_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = int(get_jwt_identity())
    
    transactions = Transaction.query.filter_by(user=user_id).order_by(Transaction.created_at.desc()).all()
    
    return jsonify({
        'transactions': [t.to_dict() for t in transactions]
    }), 200
    
@transaction_bp.route('/transactions', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    
    if not data or not data.get('reference') or 'amount' not in data:
        return jsonify({'error': 'Missing required fields: reference, amount'}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    amount = float(data['amount'])
    if user.balance + amount < 0:
        return jsonify({'error': 'Insufficient balance'}), 400
    
    previous_balance = user.balance
    user.balance += amount
    
    transaction = Transaction(
        reference=data['reference'],
        user=user_id,
        previous_balance=previous_balance,
        amount=amount,
        balance=user.balance
    )
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({
        'message': 'Transaction created successfully',
        'transaction': transaction.to_dict(),
        'current_balance': user.balance
    }), 201


