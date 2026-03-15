import os
import json
import shutil
import sys
from pathlib import Path
from PIL import Image

# Constants for project structure
PROJECT_NAME = "Wallpaper Engine Project"
ASSETS_DIR = "assets"
CONFIG_FILE = "project.json"
ICONS_DIR = "icons"
PREVIEW_IMAGE = "preview.jpg"

# Function to create the project folder structure

def create_project_structure(base_path):
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(base_path / ASSETS_DIR, exist_ok=True)
    os.makedirs(base_path / ICONS_DIR, exist_ok=True)

# Function to generate the project.json configuration

def generate_config(base_path):
    config = {
        "project_name": PROJECT_NAME,
        "icon": str(base_path / ICONS_DIR / "icon.ico"),
        "preview": str(base_path / PREVIEW_IMAGE),
        "assets": str(base_path / ASSETS_DIR)
    }
    with open(base_path / CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

# Function to copy executable files

def copy_executables(base_path):
    executables = ["executable1.exe", "executable2.exe"]  # Add actual executables
    for exe in executables:
        try:
            shutil.copy(exe, base_path)
        except Exception as e:
            print(f"Error copying {exe}: {e}")

# Function to generate icon from PNG

def generate_icon_from_png(png_path, icon_path):
    try:
        img = Image.open(png_path)
        img.save(icon_path, format='ICO')
    except Exception as e:
        print(f"Error generating icon: {e}")

# Function to generate preview image from source

def generate_preview_image(source_path, preview_path):
    try:
        img = Image.open(source_path)
        img.save(preview_path, "JPEG")
    except Exception as e:
        print(f"Error generating preview image: {e}")

# Function to handle command-line arguments

def handle_arguments():
    if len(sys.argv) < 2:
        print("Usage: python setup_wallpaper_project.py <project_directory>")
        sys.exit(1)
    return Path(sys.argv[1])

# Main function

def main():
    project_directory = handle_arguments()
    create_project_structure(project_directory)
    generate_config(project_directory)
    copy_executables(project_directory)
    generate_icon_from_png(project_directory / "source.png", project_directory / ICONS_DIR / "icon.ico")
    generate_preview_image(project_directory / "source_image.jpg", project_directory / PREVIEW_IMAGE)
    print("Wallpaper Engine project setup complete.")

if __name__ == '__main__':
    main()