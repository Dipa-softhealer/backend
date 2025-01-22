# WAP to add two matrices using nested loop
# 3Y + (X + 2Y) + (5Z + 4X)

x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]
z = [[0,8,4],[6,9,3],[9,1,9]]
res = []
# the equation is like : 3Y + (X + 2Y) + (5Z + 4X)

for i in range(3):
    temp = []
    for j in range(3):
        temp.append(y[i][j]*3 + (x[i][j] + y[i][j]*2) + (z[i][j]*5 + x[i][j]*4))
    res.append(temp)

print(res)


# Y3 =[]
# for i in y:
#     temp=[]
#     for j in i :
#         temp.append(j*3)
#     Y3.append(temp)
    
# Y2 =[]
# for i in y:
#     temp=[]
#     for j in i :
#         temp.append(j*2)
#     Y2.append(temp)

# Z5 =[]
# for i in z:
#     temp=[]
#     for j in i :
#         temp.append(j*5)
#     Z5.append(temp)
    
# X4 =[]
# for i in x:
#     temp=[]
#     for j in i :
#         temp.append(j*4)
#     X4.append(temp)
     
# # for x + Y2
# res1=[]
# for i in range(3):
#     temp = []
#     for j in range(3):
#         temp.append(x[i][j] + Y2[i][j])
#     res1.append(temp)
# # print(res1)

# res = []
# for i in range(3):
#     temp = []
#     for j in range(3):
#         temp.append(res1[i][j]+Y3[i][j])
#     res.append(temp)
# # print(res)

# res2 = []
# for i in range(3):
#     temp = []
#     for j in range(3):
#         temp.append(Z5[i][j]+X4[i][j])
#     res2.append(temp)
# print(res2)

# res3 = []
# for i in range(3):
#     temp = []
#     for j in range(3):
#         temp.append(res[i][j]+res2[i][j])
#     res3.append(temp)
    
# txt = f"result is {res3}"
# print(txt)
