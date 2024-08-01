# square = []
# for i in range (10):
#     square.append(pow(2,i))
# print(square)

# square1 = [ pow(2,i) for i in range(10) ]
# print(square1)

# square3 = list(map(lambda x:x**2, range(10) ))
# print(square3)


input_numbers = list(map(int, input().split()))
print(input_numbers)

'''''''''
input_numbers = list(map(int, input().split()))
step1: input()

Read a string
step2: input().split()

The string read by input() is split on spaces, because default delimiter(argument) of split is space

input.split('@') # The delimiter here is '@'

12@1@124@34@57

'12', '1', '124', '34', '57'
 '''""""""