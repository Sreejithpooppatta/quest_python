# Program to find the sum of digits

import math
input_num = (input('Enter the digit '))
temp = input_num
length = log10(input_num)+1

while input_num !=0:
    reminder = input_num % 10
    input_num = input_num // 10
    sum = pow(reminder, length)
print(sum)

