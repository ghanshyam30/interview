# Form a list using for loop
some_list = list(x for x in range (0,5))

print("List for operations:",some_list)

for item in some_list:
    try:
        reciprocal = 1/item
        print(f"Reciprocal of {item} is {reciprocal}.")
    except Exception as e:
        print(f"Error: {e.__class__}")
    finally:        # Mostly used to close connection with DB
        print("I am getting executed everytime")