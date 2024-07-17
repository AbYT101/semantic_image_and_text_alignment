import os
import random
from PIL import Image

def create_ad_banner(design_concept, banner_size, logo_path, background_path, main_character_path, cta_path):
    def validate_and_open_image(image_path, required_extension=None, add_alpha_if_missing=False):
        assert os.path.exists(image_path), f'Image path does not exist: {image_path}'
        if required_extension:
            assert os.path.splitext(image_path)[1].lower() == required_extension, f'Image must be a {required_extension} file: {image_path}'
        image = Image.open(image_path).convert('RGBA')
        if add_alpha_if_missing and 'A' not in image.getbands():
            alpha = Image.new('L', image.size, 255)
            image.putalpha(alpha)
        return image

    def random_transform_foreground(foreground, background_size, rotate=True):
        if rotate:
            angle_degrees = random.randint(0, 359)
            foreground = foreground.rotate(angle_degrees, resample=Image.BICUBIC, expand=True)
        
        scale = random.random() * 0.5 + 0.5
        new_size = (int(foreground.size[0] * scale), int(foreground.size[1] * scale))
        foreground = foreground.resize(new_size, resample=Image.BICUBIC)
        
        max_xy_position = (background_size[0] - foreground.size[0], background_size[1] - foreground.size[1])
        assert max_xy_position[0] >= 0 and max_xy_position[1] >= 0, 'Foreground is too big for the background'
        paste_position = (random.randint(0, max_xy_position[0]), random.randint(0, max_xy_position[1]))

        return foreground, paste_position

    banner_width, banner_height = banner_size

    background = validate_and_open_image(background_path)
    background = background.resize(banner_size).convert('RGBA')
    
    logo = validate_and_open_image(logo_path, required_extension='.png', add_alpha_if_missing=True)
    main_character = validate_and_open_image(main_character_path, required_extension='.png', add_alpha_if_missing=True)
    cta = validate_and_open_image(cta_path, required_extension='.png', add_alpha_if_missing=True)

    logo, logo_pos = random_transform_foreground(logo.resize((int(banner_width / 5), int(banner_height / 5))), banner_size)
    main_character, main_character_pos = random_transform_foreground(main_character.resize((int(banner_width / 2), int(banner_height / 2))), banner_size, rotate=False)
    cta, cta_pos = random_transform_foreground(cta.resize((int(banner_width / 5), int(banner_height / 5))), banner_size)
    
    banner = Image.new('RGBA', banner_size)
    banner.paste(background, (0, 0))
    banner.paste(logo, logo_pos, logo)
    banner.paste(main_character, main_character_pos, main_character)
    banner.paste(cta, cta_pos, cta)

    return banner
