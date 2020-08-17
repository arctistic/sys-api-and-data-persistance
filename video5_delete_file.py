import os
from pathlib import Path

file_path = Path('.')
file_name = Path('my_file.txt')

if os.path.exists(file_path) and os.path.isdir(file_path):
    if os.path.exists(file_path/file_name) and os.path.isfile(file_path/file_name):
        print('File found! Deleting ...')
        os.remove(file_path/file_name)
    else:
        print('File not found, nothing to do!')
else:
    print('Invalid Directory specified')
