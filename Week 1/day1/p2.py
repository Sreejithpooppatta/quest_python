# # accept the food item number from the user and serve him the food

# # food_item = {
# #     1: 'Mysoor special cofee',
# #     2: 'Tamilnadu special dosa',
# #     3: 'Kerala special Sewa',
# #     4: 'Bhopal special poha',
# #     5: 'Bengaluru special upma'
# # }
# # print('Welcome to Rameshwaram cafe')
# # print('1: Cofee 2: Idily 3:Dosa 4: Sewa 5:Upma')
# # Food_item_num = int(input('accept the food item number'))
# # if Food_item_num in range (0, 6):
# #     print('your ordered food '+ food_item.get(Food_item_num) + 'is here'  )
# #     print('Thank you and visit again')
   
# # else:
# #      print("Invalid input")



# #Accept the food item number from the user and serve him the food.
# import sys
# veg_food_items = { 
#     1 : 'Mysuru Filter Coffee',
#     2 : 'Yummy Idly-vada', 
#     3 : 'Worlds soft Mysuru Mailari Dosa', 
#     4 : 'Bhupal Special Poha', 
#     5 : 'Bengaluru tamato-peanuts Upama' 
# }

# non_veg_food_items = { 
#     1 : 'Egg Pokoda',
#     2 : 'Chicken Biryani', 
#     3 : 'Fish Fry', 
#     4 : 'Mutton Masala' 
# } 

# food_types = { 
#     1 : veg_food_items, 
#     2 : non_veg_food_items 
# } 
# food_items = { 
#     1 : '1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama', 
#     2 : '1:Egg Pokoda 2:Chicken Biryani 3:Fish Fry  4: Mutton Masala'
# } 
# print('Welcome to our hotel The Taste') 
# user_choice = int(input('1:Veg 2:Non-Veg \t Your choice please: '))
# items = food_items.get(user_choice, 'Invalid') 
# if items == 'Invalid': 
#     sys.exit('Invalid choice entered')

# print(items) 
# food_item_number = int(input('Enter the food item number that you wish:')) 
# print('Your ' + food_types.get(user_choice) + ' is here') 
# print('Thank you, Visit again')


