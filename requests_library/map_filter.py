# list creation using simple list comprehenssion
list1 = [x for x in range(0,10)]
print("Original list:",list1)

# filter out only elements whose value is greater than 5
# Syntax goes like : filter_object = filter(lambda item_from_list, condition for item, list_to_operate_on)
filter_object = filter(lambda x: x>5,list1)
print("Filtered list:",list(filter_object))

# map 
map_object = map(lambda x, x>5,list1)
print("Map object:",list(map_object))