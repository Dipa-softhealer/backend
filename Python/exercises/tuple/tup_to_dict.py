# convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
my_dict = {}
def apd(key,number) :
    if key in my_dict:
        my_dict[key].append(number)
    else:
        my_dict[key] = [number]  # Create a new list if the key doesn't exist


for i in l :
    apd(i[0],i[1])       


print(my_dict)