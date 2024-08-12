class age_gender:
    def __init__(self, age, gender, residence, pincode, pin):
        self.age = age
        self.gender = gender
        self.residence = residence
        self.pincode = pincode
        self.pin = pin

    def men_condition(self):
        pass
    def women_condition(self):
        pass

class Men(age_gender):
    def men_condition(self):
        conditions_local = [
            (self.age >= 60 and self.gender == "m" and self.residence == 'l' and occupation == 'w', '25% discount on all products for localite working men'),
            (self.age < 60 and self.gender == "m" and self.residence == 'l' and occupation == 'w', '30% discount on Smart Phones and Laptops for localite working men'),
            (self.age in range(5, 31) and self.gender == "m" and self.residence() == 'l' and occupation == 's', '25% discount on all products and 50% discount for books for localite student')
        ]
        conditions_hostel = [
            (self.age >= 60 and self.gender == "m" and self.residence == 'h' and occupation == 'w', '30% discount on all products for hostelers working men'),
            (self.age < 60 and self.gender == "m" and self.residence == 'h' and occupation == 'w', '35% discount on Smart Phones and Laptops for hostelers working men'),
            (self.age in range(5, 31) and self.gender == "m" and self.residence == 'h' and occupation == 's', '40% discount on all products and 50% discount for books for hostelers student')
        ]

        for i  in range(len(conditions_local)):
            if conditions_local[i][0]:
                print(conditions_local[i][1])
                return

        if self.pin in self.pincode:
            for j  in range(len(conditions_hostel)):
                if conditions_hostel[j][0]:
                    print(conditions_local[j][1])
                    return

        print("No applicable mens discounts found .")

class Women(age_gender):
    def women_condition(self):
        conditions_local = [
            (self.age >= 45 and self.gender == "f" and self.residence == 'l' and occupation == 'w', '25% discount on all products for localite working women'),
            (self.age < 60 and self.gender == "f" and self.residence == 'l' and occupation == 'w', '30% discount on Nyka and Clothings for localite working women'),
            (self.age in range(5, 31) and self.gender() == "f" and self.residence == 'l' and occupation == 's', '25% discount on Nyka and 50% discount for books for localite women student')
        ]
        conditions_hostel = [
            (self.age >= 60 and self.gender == "f" and self.residence == 'h' and occupation == 'w', '30% discount on all products for hostelers working women '),
            (self.age < 60 and self.gender == "f" and self.residence == 'h' and occupation == 'w', '35% discount on Nyka and Clothing for hostelers working women'),
            (self.age in range(5, 31) and self.gender == "f" and self.residence == 'h' and occupation == 's', '40% discount on Nyka and 50% discount for books for hostelers women student')
        ]

        for i  in range(len(conditions_local)):
            if conditions_local[i][0]:
                print(conditions_local[i][1])
                return

        if self.pin in self.pincode:
            for j  in range(len(conditions_hostel)):
                if conditions_hostel[j][0]:
                    print(conditions_local[j][1])
                    return
                
        print("No applicable women discounts found .")




try:
    age = int(input("Enter age: "))
    gender = input("Enter gender: \nM for Male\nF for Female\nO for Other\nEnter: ").lower()
    residence = input("Are you Localite or Hostler: \nL for Localite\nH for Hostler\nEnter: ").lower()
    occupation = input("Enter occupation: \nW for Working\nS for Student\nEnter: ").lower()
    pincode = [123456, 234567, 345678]
    pin = int(input('Enter your pin: '))
except ValueError as e:
    print(f'{e}  enter valid values for marks.')
else:
    m = Men(age, gender, residence, pincode, pin)
    m.men_condition()

    w = Women(age, gender, residence, pincode, pin)
    w.women_condition()
