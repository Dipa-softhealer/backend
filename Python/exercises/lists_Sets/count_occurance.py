# count occurrences element list 

list = [15, 6, 7, 10, 12, 20, 10, 28, 10,6]
el = 10
count = 0
# for i in list :
#     if i == el :
#         count+= 1
# print(f"output : {count}")

# try to convert the same in 
count = [1 for i in list if i == el]
print(f"output : {sum(count)}")
