# 10- Riya was planning to invent a game of shifting

def shifting_game (input_rows,input_columns):

    matrix = []

    for i in range(input_rows):
        print(f'Enter {input_columns} numbers of Row-{i+1}')
        row_numbers = [] 
        for j in range(input_columns): 
            row_numbers.append(int(input()))
        matrix.append(row_numbers)

    print('\n\n-- Before shifting --')

    for rows in matrix:
        for number in rows:
            print('%-3s'%(number), end='')
        print()


    shifted_matrix = []

    for i in range(input_rows):
        row_numbers = []
        for j in range(input_columns):
            row_numbers.append(matrix[j][i])
        shifted_matrix.append(row_numbers)

    print('\n\n-- After shifting --')

    for row in shifted_matrix:
        for number in row:
            print('%-3s'%(number), end='')
        print()



input_rows = int(input('Enter number of rows of the matrix: '))
input_columns = int(input('Enter number of columns of the matrix: '))

shifting_game (input_rows,input_columns)