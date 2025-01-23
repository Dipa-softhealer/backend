# reversing the given list
x = [10, 11, 12, 13, 14, 15]
x = ([x[i] for i in range(len(x)-1,-1,-1)])
print(x)