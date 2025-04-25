from app.extensions import db
from datetime import datetime

class TokenBlocklist(db.Model):
    __tablename__ = 'blocklist'
    
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'<TokenBlocklist {self.jti}>'

    def to_dict(self):
        return {
            'id': self.id,
            'jti': self.jti,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    
