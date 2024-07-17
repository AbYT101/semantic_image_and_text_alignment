from flask import Blueprint, request, jsonify
from services.evaluate_service import evaluate_image

bp = Blueprint('evaluate', __name__)

@bp.route('/evaluate', methods=['POST'])
def evaluate():
    file = request.files.get('file')
    imageAnalyzer = request.form.get('imageAnalyzer')
    description = request.form.get('description')
    if not file or not description or not imageAnalyzer:
        return jsonify({"error": "File, Image Analyzer or description not provided"}), 400

    try:
        evaluation_result = evaluate_image(file, imageAnalyzer, description)
        return jsonify({"message": "Image evaluated successfully", "result": evaluation_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
