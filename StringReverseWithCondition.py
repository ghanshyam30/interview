"""
Problem: parse the given string and reverse all the characters but leave the non-characters  at their own index
example input: "ab<c"
example output: "cb<a"
Test input: a$$csd@#efgh****
Test output: h$$gfe@#dsca****
"""
# string_given = "abcd<efgh"
string_given = input("Enter string:")

arr = list(string_given)
print(arr)
alpha_arr = []
result_arr = [None for x in range(0,len(arr))]
counter = 0
for item in arr:
    if item.isalpha():
        alpha_arr.append(item)
        print(f"for {item}, alpha array:{alpha_arr}")
    else:
        result_arr[counter] = item
        print(f"for {item}, result array:{result_arr}")
    counter += 1

reverse_string = alpha_arr[::-1]
# print(reverse_string)
# print(result_arr)
alpha_counter = 0
for result_index in range (0,len(arr)):
    if result_arr[result_index] == None:
        # print("Index:",result_index)
        result_arr[result_index] = reverse_string[alpha_counter]
        alpha_counter = alpha_counter + 1

result = ""
for item in result_arr:
    result += item

print(result)
