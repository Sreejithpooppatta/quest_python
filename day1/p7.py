# Program to accept number of lines of the Triangle and draw the Trianlge:
# *
# **
# ***
# ****
# *****

input_num = int(input('Enter a  number of lines of the Triangle '))

for i in range(input_num):
    for j in range(i+1):
        print('*',end='')
    print()