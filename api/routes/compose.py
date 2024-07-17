import os
from flask import Blueprint, request, jsonify, send_file
from services.compose_service import compose_image
from io import BytesIO

bp = Blueprint('compose', __name__)

@bp.route('/compose', methods=['POST'])
def compose():
    # Ensure all required files are provided
    required_files = ['logo', 'main_character', 'background', 'cta']
    missing_files = [file for file in required_files if file not in request.files]

    if missing_files:
        return jsonify({"error": f"Missing files: {', '.join(missing_files)}"}), 400

    # Extract files from the request
    logo = request.files['logo']
    main_character = request.files['main_character']
    background = request.files['background']
    cta = request.files['cta']
    description = request.form.get('description', '')
    banner_size = (800, 400)  # Example size, adjust as needed

    try:
        # Call compose_image function
        composed_image = compose_image(description, banner_size, logo, background, main_character, cta)

        # Return the composed image
        return send_file(
            BytesIO(composed_image),
            mimetype='image/png',
            as_attachment=True,
            download_name='composed_image.png'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
