class eatable:
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.isPeelable = isPeelable
        self.isBoneless = isBoneless

    def food_type(self):
        return "eatable"

class vegetarian(eatable):
    def food_type(self):
        print('\nVegetarian')
        print(f'carbs is {carbs}\nfat is {fat}\nprotein is {protein}\npeelable {isPeelable}\n ')
       
class nonvegetarian(eatable):
    def food_type(self):
        print('Non Vegetarian')
        print(f'carbs is {carbs}\nprotein is {protein}\nboneless {isBoneless} ')

def constrains (): 

    if isPeelable == 'yes':
        veg = vegetarian("carbs", "fat", "protein", "isPeelable", "isBoneless")
        veg.food_type()
    else:
        print('input values are not  vegetarian')
    if isBoneless == 'yes':
        nonveg = nonvegetarian("carbs", "fat", "protein", "isPeelable", "isBoneless")
        nonveg.food_type()
    else:
        print('input values are not for non vegetarian')
        

try:

    carbs = int(input('enter for carbs in grams '))
    fat = int(input('enter for fat in grams '))
    protein = int(input('enter for protein in grams '))
    isPeelable = (input('enter for isPeelable yes or no  ')).lower()
    isBoneless = (input('enter for isBoneless yes or no  ')).lower()
    constrains()

except ValueError as e:
    print(f'Enter numeric values {e} not accepted')
    





 
