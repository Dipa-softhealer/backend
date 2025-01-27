# Bracket Matcher

inp = "(h(e)llo)(world)"
# pop untill got ")"
def bracketMatcher(str):
    lst0 = []
    lst1 = []
    n = range(len(str))
    for i in n :
        if(inp[i] == ")"):
            lst0.append(0)
        elif(inp[i] == "("):
            lst1.append(1)
        
    return int(len(lst0)== len(lst1))

res = bracketMatcher(inp)
print(res)