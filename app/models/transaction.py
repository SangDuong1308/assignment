from app.extensions import db
from datetime import datetime
import uuid

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(64), nullable=False, default=lambda: str(uuid.uuid4()))
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    previous_balance = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'<Transaction {self.reference}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'reference': self.reference,
            'user_id': self.user,
            'previous_balance': self.previous_balance,
            'amount': self.amount,
            'balance': self.balance,
            'created_at': self.created_at.isoformat()
        }
        
        
