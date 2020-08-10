# Intention
# How to unpack the dictionary
# How to pass dictionary as an argument to the function accepting kwrgs and not normal variable passing

# Basic code
def funcion_accepting_kwrgs(a,b,**individual_param):
    for x,y in individual_param.items():
        print(f"key is {x} and value is {y}")

# Notic "KEYS" are not having any quotes while passing as individual pair for kwrgs
funcion_accepting_kwrgs("random",2,name="Some coder",level="Not so good",review="average",result = False)



# Advanced code
def funcion_accepting_kwrgs_as_dict(**dict_param):
    # print(x.key() for x in dict_param.items())
    for x,y in dict_param.items():
        print(f"key is {x} and value is {y}")

dictionary_to_pass = {
    "name" : "Some coder",
    "level" : "Not so good",
    "review" : "average",
    "result" : False 
}

# when passing a dictionary as parameter to a function accepting kwrgs we need to prepend it by **
funcion_accepting_kwrgs_as_dict(**dictionary_to_pass)


# Unpacking of dictionary
unpack_this = { "id" : 324234, "name": "python advanced"}

#1
# We need to call items method for unpacking of dictionary
print("Unpacking using items will give tuple in return")
a, b = unpack_this.items()
print(f"a={a} and b={b}")

#2 
# When we pass dictionary as it is for unpacking
a, b = unpack_this
print("Unpacking dict as it is")
print(f"a={a} and b={b}")

#3 
# When we use values function explicitely
print("Unpacking only values")
a, b = unpack_this.values()
print(f"a={a} and b={b}")