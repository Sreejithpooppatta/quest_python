
# find nth tern of series 1 2 2 3 3 5 5 7 8 11 13 13

##########################################################################################################
import math

'''''''''

For Prime numbers

'''''''''

def isprime(input_number):                                   # To check for prime num

    def check_if_prime(num):
        for i in range(2, math.ceil(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    # input_number = int(input('Enter the number N, to print Nth Prime number: '))
    j = 0
    if input_number == 1:
        j = 2
    elif input_number == 2:
        j = 3
    else:
        count = 2
        j = 4 #Number in J is checked if Prime or not
        while count <= input_number:
            if check_if_prime(j):
                count += 1
            if count == input_number:
                break
            j += 1
    print(f'{input_number}th Prime number is {j}')

#################################################################################################################



'''''''''

For Fobo numbers

'''''''''


def isfibo(term_number):

    # term_number = int(input ("Enter N to print the Nth Fibo term: "))  

    def find_nth_fibo_term(n):
        thrid_number = 0
        first_number  = 1
        second_number = 2  
        if n == 1:
            thrid_number = 1
        elif n == 2:
            thrid_number = 2
        else:
            thrid_number  = 0
            count = 2
            while count <= n:
                thrid_number = first_number + second_number
                count += 1
                if count == n:
                    return thrid_number
                first_number = second_number
                second_number = thrid_number
        return thrid_number


    if term_number <= 0:  
        print ("Please enter a positive integer, the given number is not valid")
    else:
        print (f'The {term_number}th Fibo number is ', find_nth_fibo_term(term_number))

##############################################################################################################

'''''''''

For odd and even position

'''''''''


input_number = int(input('Enter the term to be accessed  : '))
if input_number % 2 == 0:
    position = input_number // 2
    last_prime_num  = isprime(input_number)
    print(f'{last_prime_num} is the requested number ')

else:
    position = (input_number // 2) + 1
    last_fibo_num  = isfibo(input_number)
    print(f'{last_fibo_num} is the requested number ')





