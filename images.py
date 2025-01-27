import requests
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor

# Directory to save images
SAVE_DIR = "images"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Function to generate a random string for renaming
def generate_random_name(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Fetch random image from Picsum
def fetch_picsum_image(width, height):
    image_url = f"https://picsum.photos/{width}/{height}"
    image_data = requests.get(image_url).content
    return image_data, ".jpg"

# Helper function to fetch and save a random image
def fetch_and_save_image(idx, source):
    try:
        # Random width and height between 200 and 800
        width = random.randint(200, 800)
        height = random.randint(200, 800)

        # Fetch image depending on the source
        if source == 'picsum':
            image_data, file_extension = fetch_picsum_image(width, height)
        else:
            print("Invalid source selected. Exiting...")
            return

        # Save the image to disk temporarily
        file_path = os.path.join(SAVE_DIR, f"image_{idx}{file_extension}")
        with open(file_path, "wb") as f:
            f.write(image_data)
        print(f"Downloaded {file_path}")

        # Rename the file randomly after saving
        random_name = generate_random_name()
        new_file_path = os.path.join(SAVE_DIR, f"{random_name}{file_extension}")
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {os.path.basename(new_file_path)}")

    except Exception as e:
        print(f"Error downloading image {idx}: {e}")

# Fetch images using multiple threads
def fetch_images_multithreaded(count, source):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda idx: fetch_and_save_image(idx, source), range(1, count + 1))

def main():
    print("Select image source:")
    print("1. Picsum (random placeholder images)")
    source_choice = input("Enter the number corresponding to your choice: ")

    # Validate input and choose the source
    if source_choice == "1":
        source = "picsum"
    else:
        print("Invalid choice. Exiting...")
        return

    print("Fetching and renaming random images...")
    fetch_images_multithreaded(1000, source)
    print("Download and renaming complete.")

if __name__ == "__main__":
    main()
