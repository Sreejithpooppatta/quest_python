# Remove the -ve number from a list of n numbers 
'''''''''
define a list with some -ve values 
define anothe list with same name and give the 
condition i >=0 within a loop
finally print the list

'''''''''
list1 = [1,2,3,-9,-5,5,4]
list1 = [i for i in list1 if i>=0]
print(list1)
