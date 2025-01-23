# print-duplicates-list-integers 
x = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
myDict = {}
for i in x :
    temp = i
    count = 0
    for i in x:
        if i == temp :
            count += 1        
    myDict[temp] = count

print(myDict)