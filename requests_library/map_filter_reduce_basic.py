# create a list using comprehension
list_even = [x for x in range(1,20) if x%2==0]
print(list_even)

################## FILTER  ########################

# Problem statement - filter all elements from even list which are divisible by 3
def divisible_by_3(item):
    if item %3 == 0:
        return item
    return None

filtered_list = filter(divisible_by_3,list_even)

print("Filtered List:",list(filtered_list))

#######################################################

############### MAP #######################
# Problem statement- have a list of 6 elements and find there squares

numbers_to_square = [item for item in range(7)]
print("Original list to square = ",numbers_to_square)

# Create sqared list
def square_all(item):
    return item ** 2

map_squared = map(square_all,numbers_to_square)
print("Squared numbers: ",list(map_squared))

############ MAP Ended ###############

############## ZIP ##############
number_to_square = [item for item in range (6)]
squared_numbers = [item**2 for item in number_to_square]

# function to zip
zipped_list = zip(number_to_square,squared_numbers)
print("Zipped list:",list(zipped_list))

########## ZIP on strings ############
string1_list = ['hello','I am','How']
string2_list = [' there','a bot',' are you']
string3_list = ['.','!','?']

zipped_string = zip(string1_list,string2_list, string3_list)
print("String zipped:",list(zipped_string))