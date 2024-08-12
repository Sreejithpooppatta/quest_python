class marks:
    def __init__(self, arts, maths, english, branch):
        self.arts = arts
        self.maths = maths
        self.english = english
        self.branch = branch
    
    def eligibility(self):        
        pass
    def pref(self):
        pass
    

class vacancy(marks):
    def eligibility(self):
        conditions = [
            (self.branch == 'ECE' and self.maths > 35 and self.english > 90 and self.arts > 95 , 'Eligible for the vacancy in marketing','No vacancy in marketing'),
            (self.branch == 'BCOM' and self.maths > 95 and self.english > 35 and self.arts > 35, 'Eligible for the vacancy in Accounts','No vacancy in Accounts'),
            (self.branch == 'MECH' and self.maths > 95 and self.english > 35 and self.arts > 35, 'Eligible for the vacancy in Sales','No vacancy in Sales')]

        for  i in range(len(conditions)):
            if conditions[i][0]==1:
                print(conditions[i][1])
            else:
                print(conditions[i][2])  
class pref(marks):
    def __init__(self, arts, maths, english, branch,*args):
        super().__init__(arts, maths, english, branch)
        self.args = args
    def pre(self):
        print(f'\nYour marks are -\nArts {arts}\nEnglish {english}\nMaths{maths}\n Your branch is- {branch} ')
        print (f'your preference are {self.args} ')

try:
    arts = int(input('Enter the marks of arts: '))
    maths = int(input('Enter the marks of maths: '))
    english = int(input('Enter the marks of english: '))
    branch = input('Enter your branch\nece\nmech\nbcom\n:- ').upper()
except ValueError as e:
    print(f'{e} Please enter valid numeric values for marks.')
else:

    try:
        preference1 = input('Enter your 1st preference \nMarketing \nAccounts \nSales:\n:- ').lower()
        preference2 = input('Enter your 2nd preference \nMarketing \nAccounts \nSales:\n:- ').lower()
        if preference1 not in ['marketing', 'accounts', 'sales' ] or preference2 not in ['marketing', 'accounts', 'sales' ]:
            raise ValueError("Preferences must be Marketing, Accounts, Sales.")
    except ValueError as e:
        print(f"{e} Please enter valid  term for preferences.")
    else:
        p = pref( arts, maths, english, branch,preference1, preference2)
        p.pre()
        s = vacancy(arts, maths, english, branch)
        s.eligibility()
        
