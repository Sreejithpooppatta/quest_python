# vyasa sister loves array

def descending_order_array(numbers):
 
  numbers.sort(reverse=True)
  return numbers

number_of_test_cases = int(input("Enter the number of test cases: "))

for i in range(number_of_test_cases):
  
  array_size = int(input("Enter the size of the array: "))

  numbers = list(map(int, input("Enter the elements: ").split()))

  sorted_numbers = descending_order_array(numbers)

  print(sorted_numbers)
