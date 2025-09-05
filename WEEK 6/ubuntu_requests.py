import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def sanitize_filename(filename: str) -> str:
    """Ensure filename is safe and non-empty."""
    filename = filename.strip()
    if not filename:
        return "downloaded_image.jpg"
    return filename.replace(" ", "_")

def get_unique_filename(filepath: Path, content: bytes) -> Path:
    """
    Prevent duplicate downloads by hashing content.
    If an identical file exists, return its path instead of creating a new one.
    """
    file_hash = hashlib.md5(content).hexdigest()
    for existing_file in filepath.parent.glob("*"):
        if existing_file.is_file():
            with open(existing_file, "rb") as f:
                if hashlib.md5(f.read()).hexdigest() == file_hash:
                    return existing_file
    return filepath

def fetch_image(url: str, save_dir: Path) -> None:
    """Fetch and save an image from the given URL."""
    try:
        # Fetch image
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check if response is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: {url} (not an image)")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = sanitize_filename(os.path.basename(parsed_url.path))
        if not filename or "." not in filename:
            ext = content_type.split("/")[-1] or "jpg"
            filename = f"downloaded_image.{ext}"

        filepath = save_dir / filename

        # Prevent duplicate downloads
        filepath = get_unique_filename(filepath, response.content)

        if filepath.exists():
            print(f"✓ Already exists: {filepath.name}")
            return

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filepath.name}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory
    save_dir = Path("Fetched_Images")
    save_dir.mkdir(exist_ok=True)

    # Get one or multiple URLs
    urls = input("Please enter image URLs (comma-separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url, save_dir)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
