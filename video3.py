import sys
# print('sys.argv is', sys.argv)

count = 0
for line in sys.stdin:
    count += 1
    # in each 'line', there is a white space at the front
    # and a '\n' at the every end
    # therefore a 'hello' will become ' hello\n'
    line = line[:-1].strip() # removing space and '\n'
    print('line: '+line+' | char-count:'+str(len(line)))
    if line == 'quit':
        break
print(count)