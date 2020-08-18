import platform
import ctypes, os, sys

try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print ('User is admin?',is_admin)
print('Version of Python :', platform.python_version())
print('system            :', platform.system())
print('release           :', platform.release())
print('version           :', platform.version())
print('machine           :', platform.machine())
print('node              :', platform.node())
print('Endian-ness       :',sys.byteorder)