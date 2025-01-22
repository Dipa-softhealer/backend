# 7) From a given list of natural numbers, return the two closest numbers.
ch = ''
InputList = []

while ch != "q" :
    ch = input("type q for quit and No. otherwise : ")
    if(ch == "q"):
        break
    InputList.append(int(ch))
if (len(InputList) == 0):
    InputList = [3, 9, 50, 15, 99, 7, 98, 65]
InputList.sort()
n = len(InputList)
minVal = InputList[len(InputList)-1]
OutputList = []
for i in range(1,len(InputList)):
    # print(minVal,InputList[i]-InputList[i-1])
    if(InputList[i]-InputList[i-1] < minVal):
        minVal = InputList[i]-InputList[i-1]
        OutputList = [InputList[i-1],InputList[i]]
print(OutputList)