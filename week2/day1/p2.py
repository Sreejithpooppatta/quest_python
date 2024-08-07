age = int(input("Enter age: "))
gender = input("Enter gender: \nM for  Male\nF for Female\nO for Other\nEnter any number.")
occupation = input("Enter occupation: \nW for Working and Non Working\nS for student\nEnter ")
residence = input("Are you Localite or Hostller: \nL for Localite\nH for Hostller\nEnter ")
pincode = input('Enter pincode  ')


if age >= 60 and gender.lower() == "m" and residence.lower() == 'l'and len(pincode) == 6:
    print('For men Localite above age 60')
    if occupation.lower() == 'w':
        print('25% discount on all product')
    elif occupation.lower() == 's':
        print('25% discount on all product and 50% discount for books')
    

if age >= 60 and gender.lower() == "m" and residence.lower() == 'h':
    print('For men Hostlers above age 60')
    if occupation.lower() == 'w':
        print('35% discount on all product')
    elif occupation.lower() == 's':
        print('35% discount on all product and 70% discount for books')

if age < 60 and gender.lower() == "m" and residence.lower() == 'l' and len(pincode) == 6:
    print('For men Localite below age 60')
    if occupation.lower() == 'w':
        print('30% discount on Smart Phones and Laptops')
    elif occupation.lower() == 's':
        print('20% discount on Titan and Fastrack product')

if age < 60 and gender.lower() == "m" and residence.lower() == 'h':
    print('For men Hostlers below age 60')
    if occupation.lower() == 'w':
        print('35% discount on Smart Phones and Laptops')
    elif occupation.lower() == 's':
        print('25% discount on Titan and Fastrack product')



if age >= 45 and gender.lower() == "f" and residence.lower() == 'l' and len(pincode) == 6:
    print('For women Localite above age 45')
    if occupation.lower() == 'w':
        print('45% discount on all product')
    elif occupation.lower() == 's':
        print('50% discount on all product and 50% discount for books')

if age >= 45 and gender.lower() == "f" and residence.lower() == 'h':
    print('For women Hostlers above age 45')
    if occupation.lower() == 'w':
        print('40% discount on all product')
    elif occupation.lower() == 's':
        print('45% discount on all product and 50% discount for books')

if age < 45 and gender.lower() == "f" and residence.lower() == 'l' and len(pincode) == 6:
    print('For women Localite below age 45')
    if occupation.lower() == 'w':
        print('35% discount on Nykaa products')
    elif occupation.lower() == 's':
        print('30% discount on Nykka product and 50% discount for books')

if age < 45 and gender.lower() == "f" and residence.lower() == 'h':
    print('For women Hostlers below age 45')
    if occupation.lower() == 'w':
        print('40% discount on Nykaa product')
    elif occupation.lower() == 's':
        print('45% discount on Nykka product and 55% discount for books')









