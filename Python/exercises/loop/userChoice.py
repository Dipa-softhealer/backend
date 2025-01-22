import math
# here closest pair is one who has min diff

ch = input("Type 'q' to quit and no. otherwise : " )
myList = list()
while(ch != 'q'):
    myList.append(int(ch))
    ch = input("Type 'q' to quit and no. otherwise : " )
myList.sort()
n = len(myList)
print(myList,n)
print('Minimum Number : ',min(myList))
print('Maximum Number : ',max(myList))
if(n/2 == 0):
    print('Closest Number : ',myList[math.floor(n/2)],myList[math.ceil(n/2)-1])
else :
    print('Closest Number : ',myList[math.floor(n/2)-1],myList[math.ceil(n/2)-1])
print('Longest Number : ',myList[n-n],myList[n-1])
print('Total Sum : ',sum(myList))

print(math.floor(n/2)-1,math.ceil(n/2)-1)  # debug point 