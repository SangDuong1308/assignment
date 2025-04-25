from flask import Blueprint

healthz_bp = Blueprint('healthz', __name__)
auth_bp = Blueprint('auth', __name__)
transaction_bp = Blueprint('transaction', __name__)
staff_bp = Blueprint('staff', __name__)

from app.api import healthz, auth, transaction, staff