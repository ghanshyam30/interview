tup1 = ("hello","good")
tup2 = ("there","morning")

def add_tuples(tup_param1, tup_param2):
    added_tuple = tup1 + tup2
    print(added_tuple)

add_tuples(tup1,tup2)


# The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))