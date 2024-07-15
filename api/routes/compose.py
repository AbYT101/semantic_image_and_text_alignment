from flask import Blueprint, request, jsonify
from services.compose_service import compose_image

bp = Blueprint('compose', __name__)

@bp.route('/compose', methods=['POST'])
def compose():
    # Check if files were sent in the request
    if 'files' not in request.files:
        return jsonify({"error": "No files provided"}), 400

    # Extract files from the request
    files = request.files.getlist('files')

    # Ensure at least one file is provided
    if len(files) == 0:
        return jsonify({"error": "No files provided"}), 400

    # Extract description (if provided)
    description = request.form.get('description', '')

    try:
        # Call your compose_image function passing files and description
        composed_image = compose_image(files, description)

        # Return success response
        return jsonify({"message": "Image composed successfully", "image": composed_image}), 200
    except Exception as e:
        # Return error response if compose_image function fails
        return jsonify({"error": str(e)}), 500
