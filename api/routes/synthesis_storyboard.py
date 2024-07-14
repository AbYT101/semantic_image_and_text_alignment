from flask import Blueprint, request, jsonify
from services.synthesis_storyboard_service import build_storyboard

bp = Blueprint('synthesis_storyboard', __name__)

@bp.route('/synthesis_storyboard', methods=['POST'])
def synthesis_storyboard():
    files = request.files.getlist('files')
    frame_descriptions = request.form.getlist('frame_descriptions')
    if not files or not frame_descriptions:
        return jsonify({"error": "Files or frame descriptions not provided"}), 400

    try:
        storyboard = build_storyboard(files, frame_descriptions)
        return jsonify({"message": "Storyboard created successfully", "storyboard": storyboard})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
