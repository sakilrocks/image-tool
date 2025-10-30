
from PIL import Image
import os
from .utils import get_output_path

def compress_image(path, quality=70, output=None):
    try:
        img = Image.open(path)
        output = output or get_output_path(path, "compressed")

        # for PNG/WebP, handle separately

        format = img.format if img.format != "PNG" else "PNG"
        img.save(output, format=format, optimize=True, quality=quality)
        print(f"compressed: {os.path.basename(path)} -> {os.path.basename(output)}")
    except Exception as e:
        print(f"failed to compress {path}: {e}")