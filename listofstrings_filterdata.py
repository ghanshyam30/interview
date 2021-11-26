"""
String[] dateArray = {"20/Jun/2020", "01/Apr/2020", "18/Dec/2019"}
output : Apr Jun Dec
"""
dateArray = ["20/Jan/2020", "01/Mar/2020", "18/Feb/2019"]
split_array = []
for element in dateArray:
	split_elemt = element.split("/")    # ["20","Jan","2020"]
	split_array.append(split_elemt)      # split_array = [["20","Jan","2020"],----]

print(split_array)

months = []
for split_item in split_array:
    months_item = split_item[1] 
    months.append(months_item)      # month = ["Jan", --]

print(months)

enumberate_moths = list(enumerate(["Jan","Feb","Mar"],1))

print(list(enumberate_moths))
sorted_months = list(map(lambda x: x[1],sorted(list(enumberate_moths), key= lambda item:item[0])))
print(sorted_months)     #["Apr", "Jun", "Dec"]
string_months = ""
for item in sorted_months:
    string_months += item + " "
print(string_months)
# Good use of sorted and lambda
# sorted_months = sorted(split_array,key=lambda item: item[1])
# print(sorted_months)