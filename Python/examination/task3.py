# Count Occurrences in List

inp =  [10, 20, 30, 10, 10, 20, 40, 50]
my_dict = {}
for i in inp:
    count = 0
    tmp = i
    count = [1 for i in inp if i == tmp]
    count = sum(count)
    my_dict[tmp] = count
    
# this line of code for remove duplicates fro list
inp = set(inp)
inp = list(inp)
# sorting the list
inp.sort()
for i in inp:
    print(f" {i} appears {my_dict[i]} times",end=" ")
