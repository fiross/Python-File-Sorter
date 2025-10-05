
# Python File Sorter

## Author
firosit@gmail.com

## Overview
`org.py` is a Python script designed to organize files in a specified directory (such as your Downloads folder) into categorized subfolders based on file type. It helps keep your files sorted and easy to find.

## Features
- Automatically creates subfolders for Images, Documents, Music, Videos, and Others.
- Moves files into the appropriate subfolder based on their extension.
- Prints a message for each file moved and a completion message when done.

## How to Use
1. **Set the Target Folder**: Edit the `downloads_folder` variable in `org.py` to the path of the folder you want to organize.
2. **Run the Script**:
	```bash
	python org.py
	```
3. The script will create subfolders and move files accordingly.

## File Types Supported
- **Images**: jpg, jpeg, png, gif, bmp, tiff
- **Documents**: pdf, doc, docx, txt, ppt, pptx, xls, xlsx
- **Music**: mp3, wav, aac, flac
- **Videos**: mp4, mov, avi, mkv
- **Others**: Any other file types

## Example
Suppose your `downloads_folder` is set to `/home/user/Downloads`. The script will create:
- `/home/user/Downloads/Images`
- `/home/user/Downloads/Documents`
- `/home/user/Downloads/Music`
- `/home/user/Downloads/Videos`
- `/home/user/Downloads/Others`
and move files into these folders based on their type.

## Contact
For questions or support, contact: firosit@gmail.com
