import os
import random
import string

# Directory where images are saved
SAVE_DIR = "2"


# Function to generate a random string for renaming
def generate_random_name(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Function to rename all images in the SAVE_DIR
def rename_images():
    for filename in os.listdir(SAVE_DIR):
        file_path = os.path.join(SAVE_DIR, filename)

        # Check if the file is a .jpg or .gif
        if filename.endswith(('.jpg', '.gif')):
            # Generate a random name
            random_name = generate_random_name()
            new_file_path = os.path.join(SAVE_DIR, f"{random_name}{os.path.splitext(filename)[1]}")

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {os.path.basename(new_file_path)}")


def main():
    print("Renaming images...")
    rename_images()
    print("Renaming complete.")


if __name__ == "__main__":
    main()
