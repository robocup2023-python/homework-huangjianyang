import os
pathlist=os.listdir()
for i in pathlist:
    if 'python' in i:
        path=i
        pathnew=path.replace('python', 'class')
        os.rename(path, pathnew)