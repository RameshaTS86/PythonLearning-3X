#OS Module

#get current directory
import os
cd=os.getcwd()
#print(cd)
#print(os.name)

size_of_file =os.path.getsize('Testdata.txt')
if size_of_file >0:
    print('File Exists')
    print(size_of_file)
    print(os.path.getmtime('Testdata.txt'))
else:
    print('File Not Exists')