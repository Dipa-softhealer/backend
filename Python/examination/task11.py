# Word Split from Dictionary

def Word_Split(strArr):
    temp0 = strArr[0]
    temp1 = inp[1].split(",")
    lst = []
    count = 0
    while(len(temp0) != 0 and count != len(temp0)):
        count += 1
        for i in temp1:
            if(count > len(temp1)):
                break
            else:
                tmp = temp0[0:len(i)]
                if(tmp == i):
                    lst.append(tmp)
                    temp0 = temp0[(len(tmp)):]
        # print("loop ends")    # debug point
    if(len(lst) == 0):
        lst.append("not possible")
    return lst
             
# here we are using our function
inp = ["goodbyedipa", "dipa,late,apple,bat,cat,goodbye,hello,yellow,why"]
res = Word_Split(inp)
print(res)
