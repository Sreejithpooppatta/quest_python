str1 = 'sreejith'
str2 = ' '
str3 = 5
try:
    concat = str1+str2+str3
    print(concat)
except TypeError:
    print(f'cannot add an integer and a string.')

