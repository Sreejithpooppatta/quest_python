# print('123'.isdigit())  # true

# print('123python'.isdigit())  # false

# print('13.4'.isdigit())  # false

# print('123'.isdecimal())  # true

# print('3.14'.isdecimal())  # false

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3]
# list1 hast the elements of list2 in it but it does not contain list 2 
# num = 5
# if list2 in list1:
#     print('yes')
# else:
#     print('no')

# list1 = [1,2,3,4,[1,2,3],5,6,7,8,9]
# list2 = [1,2,3]

# num = 5
# if list2 in list1:
#     print('yes')
# else:
#     print('no')


# list1 = [1,2,3,4,[1,2,3],5,6,7,8,9]
# list2 = [1,2,3]

# num = 5
# if list2 not in list1:
#     print('yes')
# else:
#     print('no')
# -----------------------------------------------------------

# we can use relational operators on list objects

# l1 = [3,6,19]
# l2 = [1,2,4,12]
# if l1 > l2:
#     print('l1 is bigger')
# else:
#     print('l2 is bigger')

l1 = [3,6,19]
l2 = [1,2,4,12]
if l1.__gt__(l2):
    print('l1 is bigger')
else:
    print('l2 is bigger')

# For readability purpose we use 6 R.oprs

# > < >= <= != ==

# However we can perform any of the 6 operations using:  > and ==