import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.compose_image import create_ad_banner
import os
from tempfile import NamedTemporaryFile
from PIL import Image

def compose_image(design_concept, banner_size, logo, background, main_character, cta):
    def save_temp_file(uploaded_file):
        _, ext = os.path.splitext(uploaded_file.filename)
        temp_file = NamedTemporaryFile(delete=False, suffix=ext)
        temp_file.write(uploaded_file.read())
        temp_file.close()
        return temp_file.name

    logo_path = save_temp_file(logo)
    background_path = save_temp_file(background)
    main_character_path = save_temp_file(main_character)
    cta_path = save_temp_file(cta)

    try:
        banner = create_ad_banner(
            design_concept=design_concept, 
            banner_size=banner_size, 
            logo_path=logo_path, 
            background_path=background_path, 
            main_character_path=main_character_path, 
            cta_path=cta_path
        )

        temp_banner = NamedTemporaryFile(delete=False, suffix='.png')
        banner.save(temp_banner.name, format='PNG')
        temp_banner.close()

        with open(temp_banner.name, "rb") as image_file:
            composed_image = image_file.read()

        # Clean up temporary files
        os.remove(logo_path)
        os.remove(background_path)
        os.remove(main_character_path)
        os.remove(cta_path)
        os.remove(temp_banner.name)

        return composed_image
    except Exception as e:
        # Clean up temporary files in case of exception
        os.remove(logo_path)
        os.remove(background_path)
        os.remove(main_character_path)
        os.remove(cta_path)
        raise e