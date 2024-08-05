# 5. Accept N main strings and N sub strings into lists and check create a 
# list of numbers of 0s and 1s where 0 represents that the sub string at
# respective index is not a substring of the main string.
# main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
# sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
# presence = [1, 0, 1, 0]

main_strings = list(map(str, input('Enter the names: ').split())) # andhrapradesh kerala maharashtra haryana
sub_strings = list(map(str, input('Enter the names: ').split())) # pradesh south rashtra punjab
list = []
for i in main_strings:
    for j in sub_strings:
        if j in i:
          print('1 ',end='')
        else:
            print('0 ',end='')
        



