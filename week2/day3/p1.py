class marks:
    def __init__(self, arts, maths, english, branch):
        self.arts = arts
        self.maths = maths
        self.english = english
        self.branch = branch
    

class vacancy(marks):
    def jobs(self, arts, maths, english, branch):
        super().__init__(arts, maths, english, branch)
        
        if branch == 'ECE' and maths > 35 and english > 90 and arts > 95: 
            print('Eligible for the vacancy in marketing')

        elif branch == 'BCOM' and maths > 95 and english > 35 and arts > 35: 
            print('Eligible for the vacancy in Accounts')

        elif branch == 'MECH' and maths > 95 and english > 35 and arts > 35: 
            print('Eligible for the vacancy in Sales')
        else:
             print('NOT Eligible') 

# class pref(vacancy):
#     def job_pref(self,arts, maths, english,preference1,preference2 ) :
#         super().__init__(arts, maths, english)
#         self.preference1 = preference1
#         self.preference2 = preference2
        
try:
    arts = int(input('Enter the marks of arts: '))
    maths = int(input('Enter the marks of maths: '))
    english = int(input('Enter the marks of english: '))
    branch = input('Enter your branch\nece\nmech\nbcom\n').upper()
except ValueError as e:
    print('{e} Please enter valid numeric values for marks.')
else:

    

        s = vacancy(arts, maths, english, branch)
        s.jobs(arts, maths, english, branch)
       
