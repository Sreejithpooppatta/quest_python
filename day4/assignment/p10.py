# 3. Accept N strings and count the number of Palindromes in it.



user_input = list(map(str, input('Enter the input for palindrome: ').split()))
list1 = user_input
count = 0 
for i in range(len(user_input)):
    if user_input[i] == user_input[i][::-1]:  # Reverse the individual element
        count += 1
print(user_input)
print('number of Palindromes in it',count)















# 4. Accept N strings, and check howmany of them possess the string X



# 5. Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.



# main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
# sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']



# presence = [1, 0, 1, 0]