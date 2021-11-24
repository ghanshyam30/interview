"""
Problem - We have a list to operate on, each element of the list is a dictionary of a name of the person and certifications the persons has in single string value separated by commas.
We need to find out count of certifications that particular person has.
ex. for LMN name there are 3 certifications i.e pearl, JS, Python
So result should be 3.
Condition - Make use of LAMBDA single line function
"""
list1 = [
        {
            'name': 'XYZ',
            'certificates': 'java,php,python'
        },
        {
            'name': 'ABC',
            'certificates': 'java,c#'
        },
        {
            'name': 'LMN',
            'certificates': 'perl,JS,python'
        },
        {
            'name': 'HIJ',
            'certificates': 'perl,JS,python'
        },
        {
            'name': 'EFG',
            'certificates': 'perl,JS,python'
        }
    ]

# Print input as it is
print(list1)

# Lambda function - non correct way
# result = len(list(map(lambda item: item["certificates"] if item["name"]== "LMN" else None, list1))[2].split(","))

# perfect solution
result = len(list(map(lambda item: item["certificates"],filter(lambda item: item["name"]== "LMN", list1)))[0].split(","))
print(result)

# Details about perfect solution
# Filter will get us only matching record which will be dictionary with all the record attributes i.e name, cert, also anything else that it has
# Map will allow us to operate on filter object to get only certificates attribute value from filtered record object
# Then we will convert this certificates value as List element
# will access this only list element as [0] index and split it with "," 
# we can get length of the splitted list