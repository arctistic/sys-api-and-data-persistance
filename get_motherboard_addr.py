import platform
from subprocess import Popen, PIPE

p = Popen('wmic bios get serialnumber', stdin=PIPE, stdout=PIPE, stderr=PIPE)
serial_num_output, serial_num_err = p.communicate()
print(serial_num_output.decode('utf-8'))
return_code = p.returncode
print('Return Code: ', return_code)