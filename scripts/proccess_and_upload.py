import os
import glob
from PIL import Image
import requests

IN_DIR = "incoming"
OUT_DIR = "processed"

def ensure_dirs():
    os.makedirs(OUT_DIR, exist_ok=True)

def process_image(src_path):
    img = Image.open(src_path).convert("RGB")
    img.thumbnail((2000, 2000))

    base = os.path.splitext(os.path.basename(src_path))[0]
    out_path = os.path.join(OUT_DIR, f"{base}.jpg")
    img.save(out_path, "JPEG", quality=82, optimize=True)
    return out_path

def main():
    ensure_dirs()

    images = []
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        images.extend(glob.glob(os.path.join(IN_DIR, ext)))

    if not images:
        print("No images found.")
        return

    for img in images:
        print(f"Processing {img}")
        process_image(img)

if __name__ == "__main__":
    main()
