file = open('test.txt', 'r+')
lines = file.readlines()
file.seek(0)
file.write('python\n')
file.writelines(lines)
file.write('python\n')
file.close()

