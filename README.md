# image-tool

A lightweight Python command line tool to *compress*, *convert*, and *resize* images.  
Built for photographers, developers, and designers who want quick, efficient image optimization.

---

## Features

-  Compress images with adjustable quality (1–100)
-  Convert between formats (JPG, PNG, WEBP, BMP, TIFF)
-  Resize images by width and/or height
-  Batch process entire folders

 
---

## Project Structure
```
image-tool/
├── src/
│   ├── main.py
│   ├── compressor.py
│   ├── converter.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## How It Works
```
	-	compressor.py: optimizes images and reduces file size while maintaining quality.
	-	converter.py: converts between supported formats (JPEG, PNG, WEBP, BMP, TIFF)
	-	utils.py: helper functions for folder scanning and output naming.
```

---

## Usage

Compress Images
```
python src/main.py compress path/to/image.jpg --quality 60
```

Convert Format
```
python src/main.py convert path/to/image.png --format webp
```

Resize Image
```
python src/main.py resize path/to/image.jpg --width 800 --height 600
```

---

## Tech Stack
```
	-	Language: Python 3.8+
	-	Libraries: Pillow, argparse
```
