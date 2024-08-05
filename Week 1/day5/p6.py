import math
num_of_customers = int(input('Enter the customers '))

sum_of_bills = 0
bills = list(map(int,input(' Enter the 3 bill amount - ').split( )))

for i in bills :
    sum_of_bills += i
root = math.sqrt(sum_of_bills)

print(root)

if math.floor(root) == math.ceil(root):
    print('customer is eligible ')
else:
        print('customer is not  eligible ')



# import math

# N = int(input("The no:of customers:"))

# bill_amounts = []

# count_of_perfect_squares = 0

# print(f'Enter the bill amounts of {N} customers :')

# for i in range(N):

#     amount = int(input())

#     bill_amounts.append(amount)

# print(f'Customer bill amounts are: {bill_amounts}')

# for i in range(N):

#     root = math.isqrt(bill_amounts[i])

#     if(root * root == bill_amounts[i]):

#         count_of_perfect_squares += 1

# print(f'Count of perfect squares of {N} bills is {count_of_perfect_squares}')