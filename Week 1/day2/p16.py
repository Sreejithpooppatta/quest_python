# 9. Print a hollow square of n lines
input_row = int(input('Enter the number of rows'))
# input_col = input_row
for i in range(input_row):
    for j in range(input_row):
        if i == 0 or i == (input_row-1) or j == 0 or j == (input_row-1) : 
            print('* ',end='')
        else:
            print('  ',end='')
    print()




