# Accept n number from the user and swap the cosecutive element in the list

print('Enter the elements of list ')

list1  = list(map(int,input().split()))
print(f' List before swaping = {list1}')
temp = list1 [0]
list1 [0] = list1[1]
list1[1] = temp

print(f' List after swaping = {list1}')

