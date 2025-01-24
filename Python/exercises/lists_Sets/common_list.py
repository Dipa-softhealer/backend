# Make only one list if you have list inside list inside list.

my_list = [1,[1.1,2,[3,5,[4,5,6]],6],7,9,[5.6,[8]],9]

def myFun(lst,tmp):
    for i in lst :
        if(type(i) != list):
            tmp.append(i)
            # print(tmp)
        else:
            myFun(i,tmp)
    return tmp
res = myFun(my_list,[])
print(res)














# output = [1,1.1,2,3,6,7,9,5.6,8,9]
# temp = []
# for i in my_list:
#     if(type(i) == int):
#         temp.append(i)
#     else :
#         # in this case, as we only have list otherwise
#         for j in i :
#             temp.append(j)
# print(temp)

# temp = tuple(my_list)
# result = [i if isinstance(i, int) else myFun(i) for i in my_list]

# print("the result is ",result)