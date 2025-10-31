
import argparse
import os
from compressor import compress_image
from converter import convert_image
from utils import is_image_file, get_all_images
from PIL import Image



def resize_image(path, width=None, height=None, output=None):
    try:
        img = Image.open(path)
        orig_w, orig_h = img.size

        width = width or orig_w
        height = height or orig_h
        resized = img.resize((width, height))
        output = output or f"{os.path.splitext(path)[0]}_resized{os.path.splitext(path)[1]}"
        resized.save(output, optimize=True)
        print(f"resized: {os.path.basename(path)} -> {os.path.basename(output)}")

    except Exception as e:
        print(f"failed to resize {path}: {e}")


def process_folder(folder, func, **kwargs):
    files = get_all_images(folder)

    if not files:
        print("no images found in folder.")
        return
    for file in files:
        func(file, **kwargs)



def main():
    parser = argparse.ArgumentParser(description="image compressor & converter")
    subparsers = parser.add_subparsers(dest="command", required=True)


    # compress
    compress_parser = subparsers.add_parser("compress", help="compress image(s)")
    compress_parser.add_argument("path", help="path to image or folder")
    compress_parser.add_argument("--quality", type=int, default=70, help="compression quality (1-100)")


    # convert
    convert_parser = subparsers.add_parser("convert", help="convert image format")
    convert_parser.add_argument("path", help="path to image or folder")
    convert_parser.add_argument("--format", required=True, help="target format (jpg, png, webp, etc)")


    # resie
    resize_parser = subparsers.add_parser("resize", help="resize image(s)")
    resize_parser.add_argument("path", help="path to image or folder")
    resize_parser.add_argument("--width", type=int, help="new width in pixels")
    resize_parser.add_argument("--height", type=int, help="new height in pixels")

    args = parser.parse_args()



    if args.command == "compress":
        if os.path.isdir(args.path):
            process_folder(args.path, compress_image, quality=args.quality)
        elif is_image_file(args.path):
            compress_image(args.path, args.quality)
        else:
            print("invalid image or folder path.")

    elif args.command == "convert":
        if os.path.isdir(args.path):
            process_folder(args.path, convert_image, target_format=args.format)
        elif is_image_file(args.path):
            convert_image(args.path, args.format)
        else:
            print("invalid image or folder path.")

    elif args.command == "resize":
        if os.path.isdir(args.path):
            process_folder(args.path, resize_image, width=args.width, height=args.height)
        elif is_image_file(args.path):
            resize_image(args.path, args.width, args.height)
        else:
            print("invalid image or folder path.")

if __name__ == "__main__":
    main()

    