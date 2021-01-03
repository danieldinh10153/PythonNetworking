#!/usr/bin/env python3

import os

path = '/mnt/bd6160f6-16e5-4437-b1a4-9c5373c81d32/encrypter_temp'

files = os.listdir(path)

directory_files = len(files)

################


totalFiles = 0
totalDir = 0

# (current_path, directories in current_path, files in current_path). hence -> base, dirs, files
for base, dirs, files in os.walk(path):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))

        
##############

#for f in files: 
 #   directory_files.append(f)

#print(directory_files[0])

