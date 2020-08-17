import os
from pathlib import Path
from datetime import datetime
import pytz

# getting my current path
my_path = Path('.')
print(my_path)
file_name = Path('my_file.txt')

if os.path.exists(my_path) and os.path.isdir(my_path):
    if os.path.exists(my_path/file_name) and os.path.isfile(my_path/file_name):
        print('File exists, proceeding to update access time stamp..')
        with open(my_path/file_name,'a') as file:
            utc_zone = pytz.utc
            current_utc_time = datetime.utcnow().replace(tzinfo=utc_zone)
            file.write(str(current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))\
                +': File Updated\n')
    else:
        print('File not found, Creating it')
        with open(my_path/file_name, 'w') as file:
            utc_zone = pytz.utc
            current_utc_time = datetime.utcnow().replace(tzinfo=utc_zone)
            file.write(str(current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))\
                +': Created file\n')
    with open(my_path/file_name, 'r') as file:
        for line in file:
            print(line, end='')
# No need to close file if you use with
else:
    print('Invalid directory specified')