# convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
temp = {}
for i in l :
    temp.update({i[0]:i[1]})
print(temp)