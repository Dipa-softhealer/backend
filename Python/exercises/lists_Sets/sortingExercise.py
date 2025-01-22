
'''Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

list2 = [ 0,  1,  1,  0,  1,  2,  2,  0,  1]



Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']'''
inp = ["a", "b", "c", "d", "e", "f", "g", "h", "i",'a']
temp = [0,  1,  1,  0,  1,  2,  2,  0,  1, 0]
idx = []
mainpair = []
for i in range(len(temp)):
    mainpair.append([temp[i],inp[i]])
mainpair.sort()
inp.clear()
for i in mainpair:
    inp.append(i[1])
print(inp)