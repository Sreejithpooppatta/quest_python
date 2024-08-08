

def vacancy (branch,arts,english,maths):
    if branch == 'ECE':
        if arts > 90 and english > 90 and maths > 35:
            print('You are eligible for the vacancy in Marketing ')
        else:
            print('You are not eligible for the vacancy in Marketing')
    elif branch == 'BCOM':
        if arts > 35 and english > 35 and maths > 95:
            print('You are eligible for  the vacancy in Accounts ')
        else:
            print('You are not eligible for the vacancy in Accounts ')
    elif branch == 'MECH':
        if arts > 35 and english > 90 and maths > 90:
            print('You are eligible for the vacancy in Sales ')
        else:
            print('You are not eligible for the vacancy in Sales ')


name = input('Enter your name: ')
branch = input('Enter your branch: ').upper()


try:
    arts = int(input('Enter the marks of arts: '))
    maths = int(input('Enter the marks of maths: '))
    english = int(input('Enter the marks of english: '))
except ValueError as e:
    print(f"{e} Please enter valid numeric values for marks.")
else:
    print('Your marks are:')
    marks = {'arts': arts, 'maths': maths, 'english': english}
    print(marks)

    branch_list = ['ECE', 'MECH', 'BCOM']

    try:
        preference1 = int(input('Enter your 1st preference \n1 = Marketing \n2 = Accounts \n3 = Sales: '))
        preference2 = int(input('Enter your 2nd preference \n1 = Marketing \n2 = Accounts \n3 = Sales: '))
        if preference1 not in [1, 2, 3] or preference2 not in [1, 2, 3]:
            raise ValueError("Preferences must be 1, 2, or 3.")
    except ValueError as e:
        print(f"{e} Please enter valid numeric values for preferences.")
    else:
        preference = [preference1, preference2]

        for j in branch_list:
            for i in range(len(preference)):
                if j == branch and preference[i] == 1:
                    if arts > 90 and english > 90 and maths > 35:
                        print('You are eligible for Marketing')
                    else:
                        print('You are not eligible for Marketing')
                elif j == branch and preference[i] == 2:
                    if arts > 35 and english > 35 and maths > 95:
                        print('You are eligible for Accounts')
                    else:
                        print('You are not eligible for Accounts')
                elif j == branch and preference[i] == 3:
                    if arts > 35 and english > 90 and maths > 90:
                        print('You are eligible for Sales')
                    else:
                        print('You are not eligible for Sales')
    vacancy (branch,arts,english,maths)



