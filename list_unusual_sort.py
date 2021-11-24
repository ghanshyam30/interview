"""
Probelm - We have list of numbers but represented in string format.
The numbers are also float alike or similar to clock time ex "11:20"
We need to arrange them in ascending order of the second part only, 1st part doesn't matter.

Ex.
input = ["10:20", "11:05", "12:10", "05:30", "01:45", "09:09"]
output = ["11:05", "09:09", "12:10", "10:20", "05:30", "01:45"]  # in first element 11 doesn't matter 05 is the least of all
"""
input_list = ["10:20", "11:05", "12:10", "05:30", "01:45", "09:09"]

#Function to get the second part which we want to sort on the basis of
def sortSecond(item):
    second_item = item.split(":")[1]
    return int(second_item)

# we can provide sort method a function that can operate on the list item returns a value based on what you want to sort the list
input_list.sort(key= sortSecond)
print(input_list)