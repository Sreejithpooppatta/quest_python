# 3. Accept N strings and count the number of Palindromes in it.

user_input = list(map(str, input('Enter the input for palindrome: ').split()))
list1 = user_input
count = 0 
for i in range(len(user_input)):
    if user_input[i] == user_input[i][::-1]:  # Reverse the individual element
        count += 1
print(user_input)
print('number of Palindromes in it',count)


