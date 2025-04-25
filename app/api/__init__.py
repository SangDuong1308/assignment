from flask import Blueprint

healthz_bp = Blueprint('healthz', __name__)

from app.api import healthz