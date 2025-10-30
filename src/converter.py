
from PIL import Image
import os

def convert_image(path, target_format="jpg", output=None):
    try:
        img = Image.open(path).convert("RGB")
        base = os.path.splitext(path)[0]
        output = output or f"{base}.{target_format.lower()}"

        img.save(output, target_format.upper())
        print(f"converted: {os.path.basename(path)} -> {os.path.basename(output)}")
    except Exception as e:
        print(f"failed to convert {path}: {e}")