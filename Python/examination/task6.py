# Flatten a Nested List

inp = [[1, 2, 3], [4, 5], [6, 7, [8, 9]]]
res = []
def task6(n):
    tmp = []
    if(type(n) == list):
        for i in n :
            tmp = tmp + (task6(i))
    else :
        tmp.append(n)
    return tmp


for i in inp :
    res = res + (task6(i))
print(res)