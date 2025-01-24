# count the elements in a list until an element is a tuple.
tup = [10,20,30,(10,20),40]
count = 0
for i in tup :
    if(type(i) == tuple):
        break
    count = count + 1
print(count)