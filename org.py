import os
import shutil

# Define the directory to be organized
# Replace "C://Users//YourUsername//Downloads" with the path to your downloads folder
downloads_folder = "<Your folder name>"

# Define the subfolders for different file types
image_folder = os.path.join(downloads_folder, "Images")
docs_folder = os.path.join(downloads_folder, "Documents")
music_folder = os.path.join(downloads_folder, "Music")
videos_folder = os.path.join(downloads_folder, "Videos")
others_folder = os.path.join(downloads_folder, "Others")

# Create the subfolders if they don't exist
for folder in [image_folder, docs_folder, music_folder, videos_folder, others_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Get a list of all files in the downloads folder
files = os.listdir(downloads_folder)

# Loop through each file and move it to the correct folder
for file in files:
    # Get the full path of the file
    file_path = os.path.join(downloads_folder, file)

    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    file_ext = file.split('.')[-1].lower()

    # Move the file based on its extension
    if file_ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']:
        shutil.move(file_path, image_folder)
        print(f"Moved {file} to Images")
    elif file_ext in ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlsx']:
        shutil.move(file_path, docs_folder)
        print(f"Moved {file} to Documents")
    elif file_ext in ['mp3', 'wav', 'aac', 'flac']:
        shutil.move(file_path, music_folder)
        print(f"Moved {file} to Music")
    elif file_ext in ['mp4', 'mov', 'avi', 'mkv']:
        shutil.move(file_path, videos_folder)
        print(f"Moved {file} to Videos")
    else:
        shutil.move(file_path, others_folder)
        print(f"Moved {file} to Others")

print("File organization complete!")