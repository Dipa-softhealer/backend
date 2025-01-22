'''
By using list comprehension, 
please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

'''

givenList = [12,24,35,70,88,120,155]
newlist = [x for x in givenList if (x != givenList[0] and x != givenList[4] and x != givenList[5])]
print(newlist)