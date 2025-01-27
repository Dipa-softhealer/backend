# remove an empty tuple(s) from a list of tuples.
data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
data = set(data)
data = list(data)
# can we try unpacking ? answer is no it is tidious to implement

# next idea i have is sometihng like that, do add one more condition
for i in data :
    if(type(i) == tuple):
        if(len(i)==0):
            data.remove(i)
print(data)