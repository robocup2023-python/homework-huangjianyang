file = open('test.txt', 'r+')
lines = file.readlines()
file.close()
file = open('copy_test.txt', 'r+')
lines_copy = file.readlines()
file.close()
for i in range(len(lines)):
    if lines[i]!=lines_copy[i]:
        print(i)
