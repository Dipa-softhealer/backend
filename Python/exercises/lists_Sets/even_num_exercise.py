# Remove Even(number) element from list. 

list1 = [11, 5, 17, 18, 23, 50]
[list1.remove(x) for x in list1 if x % 2 == 0]
print(list1)