# Program to multiply two matrices using nested loops
# 3X3 matrix
X = [[12,7,3],[4 ,5,6],[7,8,9]]

# 3X4 matrix
Y = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
# resultant = 3X4
res = []

for i in range(len(X)):
    temp = []
    for j in range(len(Y[0])):
        myVar = 0
        for k in range(len(X)):
            myVar = myVar + (X[i][k] * Y[k][j])
        temp.append(myVar)
    res.append(temp)
print(res)