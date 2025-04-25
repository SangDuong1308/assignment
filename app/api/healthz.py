from app.api import healthz_bp

@healthz_bp.route('/healthz', methods=['GET'])
def health_check():
    return {"status": "ok"}

