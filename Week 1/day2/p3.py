# Program to count the number of digits in a number
# input_num = int(input('Enter the digit '))
# print('length of thr digit is',len(str(input_num)))

# input_num = int(input('Enter the digit '))
# count = 0
# temp = input_num
# while temp != 0:
#     temp = temp // 10
#     count += 1
# print(f'the odd numbers in {input_num} is {count}')



num = input('num pls')
length = len(num)
print(length)
count = 0
nump = int(num)
for i in num:
    if int(i) % 2 == 1:
        count +=1
print(count) 