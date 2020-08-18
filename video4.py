from subprocess import Popen, PIPE

p = Popen('ls -l', stdin=PIPE, stdout=PIPE, stderr=PIPE)
list_files_stdin = b''
list_files_output, list_files_err = p.communicate(list_files_stdin)
return_code = p.returncode
print(list_files_output)
print('--------------------')
print(list_files_output.decode("utf-8"))
print("The exit code was: %d" % return_code)    