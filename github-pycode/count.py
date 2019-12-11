import os
PATH ='/home/harpreet/Documents/python work/github-pycode/'
fileCount = 0
dirCount = 0
for root, dirs, files in os.walk(PATH):
    print('looking in:',root)
    for directories in dirs:
        dirCount += 1
        for Files in files:
            fileCount +=1

print('number of files', fileCount)
print('number of directories', dirCount)
print('toatal:',(dirCount + fileCount))
