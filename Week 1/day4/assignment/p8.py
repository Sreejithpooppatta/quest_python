# Problems:
# 1. User gives the data like this:
# kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
# You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]

user_input = list(map(str, input('Enter the user input').split( )))
print(user_input)

states = list(map(str, input('Enter the State').split( )))
print('The States are ', states)

capitals = list(map(str, input('Enter the user capital').split( )))
print('The Capitals are ', capitals)




































