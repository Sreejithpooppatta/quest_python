class marks:
    def __init__(self, arts, maths, english, branch):
        self.arts = arts
        self.maths = maths
        self.english = english
        self.branch = branch
    
    def eligibility(self):        
        pass
    

class vacancy(marks):
    def eligibility(self):
        if self.branch == 'ECE' and self.maths > 35 and self.english > 90 and self.arts > 95: 
            print('Eligible for the vacancy in marketing')
        elif self.branch == 'BCOM' and self.maths > 95 and self.english > 35 and self.arts > 35: 
            print('Eligible for the vacancy in Accounts')
        elif self.branch == 'MECH' and self.maths > 95 and self.english > 35 and self.arts > 35: 
            print('Eligible for the vacancy in Sales')
        else:
            print('NOT Eligible ')


try:
    arts = int(input('Enter the marks of arts: '))
    maths = int(input('Enter the marks of maths: '))
    english = int(input('Enter the marks of english: '))
    branch = input('Enter your branch\nece\nmaths\nbcom\n').upper()
except ValueError as e:
    print(f'{e} Please enter valid numeric values for marks.')
else:
    s = vacancy(arts, maths, english, branch)
    s.eligibility()
