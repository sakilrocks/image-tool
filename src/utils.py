
import os

def is_image_file(filename):
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')
    return filename.lower().endswith(valid_exts)

def get_all_images(folder_path):
    files = []
    for root, _, filenames in os.walk(folder_path):
        for f in filenames:
            if is_image_file(f):
                files.append(os.path.join(root, f))
    return files

def get_output_path(input_path, suffix):
    base, ext = os.path.splitext(input_path)
    return f"{base}_{suffix}{ext}"