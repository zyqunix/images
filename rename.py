import os

save_dir = input("images dir: ")

def rename_images():
    image_files = []
    for filename in os.listdir(save_dir):
        if filename.endswith(('.jpg', '.gif', '.png', '.jpeg')):
            image_files.append(filename)
    
    image_files.sort()
    
    for index, filename in enumerate(image_files):
        file_path = os.path.join(save_dir, filename)
        extension = os.path.splitext(filename)[1]
        new_file_path = os.path.join(save_dir, f"{index}{extension}")
        
        os.rename(file_path, new_file_path)
        print(f"Renamed {filename} to {os.path.basename(new_file_path)}")

def main():
    print("Renaming images...")
    rename_images()
    print("Renaming complete.")

if __name__ == "__main__":
    main()
