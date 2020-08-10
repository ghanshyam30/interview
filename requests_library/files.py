
# Open file for reading
file_object = open("post_api.py",'r')

#############  read file line by line  #############
for line in file_object:
    print(line)

################### Full file read #################
full_file_read = file_object.read()
print(full_file_read)

################### readlines ###############
readlines_use = file_object.readlines(5)
print(readlines_use)