# Find sum of the series: 1 + n - n(2) + n(3) - ..... m terms

# import math
# input_last_term = int(input(' Enter the mth term  '))

# input_number = int(input(' Enter a number of n  '))

# sum = 0
# sign_val = 1

# for i in range(input_last_term):
#     sum += sign_val* pow(input_number,i) 
#     sign_val *= -1

# print(f'sum of the series: {sum}')



# Find sum of the series:
# n - n(2)/3 + n(4)/5 - n(8)/7 + ..... upto m terms  and (1<=n<=5) and (2<m<10)


import math
input_last_term = int(input(' Enter the mth term  '))

input_number = int(input(' Enter a number of n  '))

sum = 0
sign_val = 1
deno = 1

if input_number in range (0,6) and input_last_term in range (2,10):
    for i in range(input_last_term):
        nume = pow(input_number, (2**i))
        sum += sign_val* (nume/deno) 
        sign_val *= -1
        deno += 2
else:
    print('invalid input')

print(f'sum of the series: {sum}')