from subprocess import PIPE, Popen

sub_process = Popen(['python','test1.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
p_output, p_error = sub_process.communicate(b'Hey')
print(p_output.decode('utf-8'))
