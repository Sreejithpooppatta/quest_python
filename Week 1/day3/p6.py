# find the smallest and biggest elements in a list

'''''''''
define a list 
set 2 variables as smallest ans largest
use min and max function method wrt to the variables
print the largest and smallest number
'''''''''''

# list1 = [10, 205, 65, 20, 115]
# smallest = min(list1)
# largest = max(list1)

# print(f"The smallest element is: {smallest}")
# print(f"The largest element is: {largest}")

# find the smallest and biggest sized string in a list

'''''''''

define a list 
set 2 variables as smallest ans largest
use min and max function method wrt to the variables 
also define key = len wrt to the list and variables
print the largest and smallest sized string
'''''''''''

list1 = ['paapu','sreejith','pooppatta','arunkolothapalli']

smallest = min(list1, key = len)
largest = max(list1, key = len)
print(f"The smallest sized string is: {smallest}")
print(f"The largest sized string : {largest}")

