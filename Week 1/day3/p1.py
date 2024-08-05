# prime numbers upto in put -

# input_num = int(input('Enter the number of series'))

# print('Prime numbers are - ')

# for i in range(2, input_num):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)



# Find last prime num -

# input_num = int(input('Enter the last digit of the series number '))

# list =[]
# print('Prime numbers are - ')

# for i in range(2, input_num):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i ,end=' ')
#         list.append(i)
# input_pos = int(input(' \n Enter the position'))
# print(f'{input_pos} prime number in the series is {list[input_pos-1]}')





# #Program to check if a number is Prime

# import math
# input_number = int(input('Enter a number to check if it is Prime: '))
# prime = True # Assume the number is Prime
# for i in range(2, math.ceil(math.sqrt(input_number)+1)):
#     if input_number % i == 0: # if N is divisible by any number other than 2 and itself
#         prime = False
#         break # break the loop
# if prime:
#     print(f'{input_number} is Prime number')
# else:
#     print(f'{input_number} is not a Prime number')



#Program to check if a number is Prime

# import math
# def check_if_prime(num):
#     for i in range(2, math.ceil(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True

# input_number = int(input('Enter the number N, to print Nth Prime number: '))
# j = 0
# if input_number == 1:
#     j = 2
# elif input_number == 2:
#     j = 3
# else:
#     count = 2
#     j = 4 #Number in J is checked if Prime or not
#     while count <= input_number:
#         if check_if_prime(j):
#             count += 1
#         if count == input_number:
#             break
#         j += 1
# print(f'{input_number}th Prime number is {j}')



# nth fibo series

# term_number = int(input ("Enter N to print the Nth Fibo term: "))  

# def find_nth_fibo_term(n):
#     thrid_number = 0
#     first_number  = 1
#     second_number = 2  
#     if n == 1:
#         thrid_number = 1
#     elif n == 2:
#         thrid_number = 2
#     else:
#         thrid_number  = 0
#         count = 2
#         while count <= n:
#             thrid_number = first_number + second_number
#             count += 1
#             if count == n:
#                 return thrid_number
#             first_number = second_number
#             second_number = thrid_number
#     return thrid_number


# if term_number <= 0:  
#     print ("Please enter a positive integer, the given number is not valid")
# else:
#     print (f'The {term_number}th Fibo number is ', find_nth_fibo_term(term_number))





    




