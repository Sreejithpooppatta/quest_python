
# file  = open("branches.txt","a")
# file.write('\ni am fine ')
# file.close()

# file  = open("branches.txt","r")
# print(file.read())

import os
import shutil
# os.chdir(r'C:\Users\sreej\OneDrive\Desktop')
# os.mkdir('a')
# os.mkdir('b')
# os.chdir('a')
# file  = open("branches.txt","x")
# file.close()
# os.chdir(r'C:\Users\sreej\OneDrive\Desktop')
# shutil.move('a/branches.txt','b')

os.chdir(r'D:\python_learning\quest_python\week2\day4')
f = open('hello.txt','x')
f.write('Hello how are you ')
f =open('hello.txt','r')
print(f.read())
f.close()


