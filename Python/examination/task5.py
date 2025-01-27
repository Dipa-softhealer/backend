# Rotate List n Positions

inp = [1,2,3,4,5,6]
n = 3
def task5(inp,n):
    subLst = inp[n:len(inp)+1]
    tmp = inp[0:n]
    res = subLst
    res = res + tmp
    return res
res = task5(inp,n)
print(res)