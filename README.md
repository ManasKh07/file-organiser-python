# file-organiser-python
Automatically organizes files into  folders according to their type using python 
# File Organizer Automation (Python)

This script automatically organizes files in a folder based on file type.

## What it does
- Reads all files from a folder
- Creates subfolders based on file extensions
- Moves files into the correct folders automatically

## Supported file types
- PDF
- TXT
- JPG / JPEG
- PNG

## How to use
1. Make sure Python is installed
2. Place the script and a folder named `python` in the same directory
3. Put your files inside the `python` folder
4. Run the script:

```bash
py organizer.py
Example
```
Before:

python/
  notes.txt
  resume.pdf
  image.jpg


After:

python/
  txt/notes.txt
  pdf/resume.pdf
  jpg/image.jpg


Output

The script prints how many files were moved after execution.
