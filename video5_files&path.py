from pathlib import Path

# home folder: the user you are runing as
# in my case Asus
print('Home folder: ', Path.home())

# print Current Working Directory
print('Current Folder: ', Path.cwd())

# creating path using pathlib.path
my_path = Path('Users', 'Asus', 'Desktop')
print('Path created: ',my_path)
print('Path created as a string: ', str(my_path))


# Joining two paths (concatination)
file_name = Path('my_file.txt')
print('joining my_path and file_name with \'/\' operator: ', my_path/file_name)


