from PIL import Image
import requests
from IPython.display import display # to display images
from pathlib import Path
import os

response = requests.get("https://www.python.org/static/img/python-logo@2x.png")
with open("python-logo.png", 'wb') as file:
    file.write(response.content)

output_path = Path('.','output')
with open('python-logo.png', 'rb') as file:
    picture = Image.open(file)
    print(picture.format)
    # picture.show() # opens image from image viewer
    greyscale_picture = picture.convert(mode='1', dither=Image.NONE)
    display(greyscale_picture)
    output_file_name = Path('python-logo-output.png')
    if os.path.isdir(output_path):
        greyscale_picture.save(output_path/output_file_name)
    else:
        os.mkdir(output_path)
        greyscale_picture.save(output_path/output_file_name)
    
