# Maximum elements in Stack

def function_for_queries(number_of_queries,stack_val):
    for element in range(number_of_queries): 

        user_input = [int(query) for query in input().split(' ')]
        
        if user_input[0] == 1:
            stack_val.append(user_input[1])

        elif user_input[0] == 2:
            del stack_val[-1]

        else:
            maximum = max(stack_val)
            print(f'The max value is {maximum}')

number_of_queries = int(input("Enter the number of queries in stack: "))

stack_val = [0]


function_for_queries(number_of_queries,stack_val)