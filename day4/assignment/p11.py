# 4. Accept N strings, and check how many of them possess the string X

user_input = list(map(str, input('Enter the names: ').split()))
alpha_to_find = input('Enter the word to find: ')
count = 0
for i in user_input:
    if alpha_to_find == i:
        count+=1
print(f'{count} possess the string {alpha_to_find} ')








# 5. Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.



# main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
# sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']



# presence = [1, 0, 1, 0]