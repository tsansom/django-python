try:
    f = open('simple.txt', 'r')
    f.write('Test write to simple.txt')
except IOError:
    print('ERROR: Not able to read or write from/to file')
else:
    print('SUCCESS!')
    f.close()
# print('hello world')
finally:
    print('I always work!')
