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
        }
    ]

# Print input as it is
print(list1)

# Lambda function
result = len(list(map(lambda item: item["certificates"] if item["name"]== "LMN" else None, list1))[2].split(","))
print(result)