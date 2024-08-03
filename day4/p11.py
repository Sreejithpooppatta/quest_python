# # 4. Accept N strings, and check how many of them possess the string X

# user_input = list(map(str, input('Enter the names: ').split()))
# alpha_to_find = input('Enter the word to find: ')
# count = 0
# for i in user_input:
#     if alpha_to_find in i:
#         count+=1
# print(f'{count} possess the string {alpha_to_find} ')





import math

x = 26
root = math.sqrt(x)
print(root)

if math.ceil(root) == math.floor(root):
    print('perfect square')
else:
    print(' not perfect square')


