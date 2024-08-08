age = int(input("Enter age: "))
gender = input("Enter gender: \nM for  Male\nF for Female\nO for Other\nEnter .")
occupation = input("Enter occupation: \nW for Working and Non Working\nS for student\nEnter ")
residence = input("Are you Localite or Hostler: \nL for Localite\nH for Hostler\nEnter ")
discountPin = [123456,1223456,123345,123445]


if age >= 60 and gender.lower() == "m" and residence.lower() == 'l'  :
    print('For men Localite above age 60')
    residencePin = int(input('Enter ur residence pin'))

    if residencePin in discountPin:
        if occupation.lower() == 'w':
            print('25% discount on all product')
        elif occupation.lower() == 's':
            print('25% discount on all product and 50% discount for books')
    else:
        print('Invalid pincode')

if age >= 60 and gender.lower() == "m" and residence.lower() == 'h' :
    print('For men Hostlers above age 60')
    if occupation.lower() == 'w':
        print('35% discount on all product')
    elif occupation.lower() == 's':
        print('35% discount on all product and 70% discount for books')

if age < 60 and gender.lower() == "m" and residence.lower() == 'l' :
    print('For men Localite below age 60')
    residencePin = int(input('Enter ur residence pin'))

    if residencePin in discountPin:
        if occupation.lower() == 'w':
            print('30% discount on Smart Phones and Laptops')
        elif occupation.lower() == 's':
            print('20% discount on Titan and Fastrack product')
    else:
        print('Invalid pincode')


if age < 60 and gender.lower() == "m" and residence.lower() == 'h' :
    print('For men Hostlers below age 60')
    if occupation.lower() == 'w':
        print('35% discount on Smart Phones and Laptops')
    elif occupation.lower() == 's':
        print('25% discount on Titan and Fastrack product')



if age >= 45 and gender.lower() == "f" and residence.lower() == 'l' :
    print('For women Localite above age 45')
    residencePin = int(input('Enter ur residence pin'))

    if residencePin in discountPin:
        if occupation.lower() == 'w':
            print('45% discount on all product')
        elif occupation.lower() == 's':
            print('50% discount on all product and 50% discount for books')
    else:
        print('Invalid pincode')




if age >= 45 and gender.lower() == "f" and residence.lower() == 'h' :
    print('For women Hostlers above age 45')
    if occupation.lower() == 'w':
        print('40% discount on all product')
    elif occupation.lower() == 's':
        print('45% discount on all product and 50% discount for books')



if age < 45 and gender.lower() == "f" and residence.lower() == 'l' :
    print('For women Localite below age 45')
    residencePin = int(input('Enter ur residence pin'))

    if residencePin in discountPin:
        if occupation.lower() == 'w':
            print('35% discount on Nykaa products')
        elif occupation.lower() == 's':
            print('30% discount on Nykka product and 50% discount for books')

    else:
        print('Invalid pincode')

if age < 45 and gender.lower() == "f" and residence.lower() == 'h' :
    print('For women Hostlers below age 45')
    if occupation.lower() == 'w':
        print('40% discount on Nykaa product')
    elif occupation.lower() == 's':
        print('45% discount on Nykka product and 55% discount for books')