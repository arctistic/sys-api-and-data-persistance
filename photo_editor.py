import requests
from PIL import Image, ImageFilter
import sys

def display_menu(filters):
    for filter_no in filters:
        if filter_no % 2 == 0:
            print(str(filter_no)+':'+filters[filter_no])
        else:
            print(str(filter_no)+':'+filters[filter_no], end=' ')
    print('')

response = requests.get('https://photos5.appleinsider.com/gallery/36935-69064-Steve-Jobs-xl.jpg')
with open('cur_photo.jpg', 'wb') as file:
    file.write(response.content)

filters = { 1:'BLUR', 2:'CONTOUR', 3:'DETAIL', 4:'EDGE_ENHANCE', 5:'EDGE_ENHANCE_MORE', \
            6:'EMBOSS', 7:'FIND_EDGES', 8:'SHARPEN', 9:'SMOOTH', 10:'SMOOTH_MORE'}
    
filters_used = []
with open('cur_photo.jpg', 'rb') as file:
    display_menu(filters)
    for line in sys.stdin:
        if line.strip() == 'SAVE':
            cur_img.save('output_img.jpg')
            break
        elif line.strip() == 'UNDO':
            with Image.open(file) as cur_img:
                cur_img = Image.open(file)
                filters_used = filters_used[:-1]
                for filter in filters_used:
                    cur_img = cur_img.filter(getattr(ImageFilter, filter))
                cur_img.show()
        else:
            with Image.open(file) as cur_img:
                line = line.strip()
                filters_used.append(filters[int(line)])
                for filter in filters_used:
                    cur_img = cur_img.filter(getattr(ImageFilter, filter))
                cur_img.show()
        display_menu(filters)
