from flask import Blueprint, request, jsonify
from services.compose_service import compose_image

bp = Blueprint('compose', __name__)

@bp.route('/compose', methods=['POST'])
def compose():
    files = request.files.getlist('files')
    if not files:
        return jsonify({"error": "No files provided"}), 400

    try:
        composed_image = compose_image(files)
        return jsonify({"message": "Image composed successfully", "image": composed_image})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
