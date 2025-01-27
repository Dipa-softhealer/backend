# Most Frequent Element Across Lists

inp = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [2, 3, 4]}
set_list = []
for i in inp.items():
    tmp = set(i[1])
    set_list.append(tmp)
# print(set_list)  # bug point

res = set_list[0] & set_list[1] & set_list[2] # according to me this is the result
res = (list(res)[0]) # DOUBT : but here 2 and 3 both are there in all dictionary values???

print(res)