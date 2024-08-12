import os
import shutil

try:
    os.chdir(r'C:\Users\sreej\OneDrive\Desktop')
    os.mkdir('a')
    os.mkdir('b')
    os.chdir('a')
    file  = open("branches.txt","x")
    file.close()
    os.chdir(r'C:\Users\sreej\OneDrive\Desktop')
    shutil.move('a/branches.txt','b')

except FileNotFoundError as e:
    print('File not found {e}')
except FileExistsError as a:
    print('File bot exist {a}')