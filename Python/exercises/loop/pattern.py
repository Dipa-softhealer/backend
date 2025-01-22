'''
write below pattern using loop


A A A A A A A
A A
A A
A A
A
A A
A A
A A
A A A A A A A




'''
row,col = 9,7

for i in range(row):
    print(end="\n")
    for j in range(col):
        if i == 0 or i == row-1 :
            print("A",end=" ")
        elif i == row//2 :
            print("A",end=" ")
            break
        else: 
            print("A A",end=" ")
            break