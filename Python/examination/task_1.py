# Find Second Largest Number
ch = ''
inp = []
while(ch !='y'):
    tmp = int(input("enter a number: "))
    inp.append(tmp)
    ch = input("do you want to quit? [y or n]")
def task1(inp):   
# first I will remove the duplicates
    inp = set(inp)
    inp = list(inp)
    inp.sort()
    inp.pop()
    return inp.pop()
res = task1(inp)
print(f"the second max number is {res} ")
