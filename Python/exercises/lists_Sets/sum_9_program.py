

'''return me list which contains lists of index whose sum is 9, no repetation
for example: 5 and 4
my_list = [3,8,5,4,6,3,1]
for eg [[2,3],[4,5] ]

'''

given_lst = [3,8,5,4,6,3,1]
n = len(given_lst)
lst_of_idx = []
sum = 9
for i in range(n):
    for j in range(n):
        if((j-i)==1):
            if(given_lst[i] + given_lst[j] == sum):
                lst_of_idx.append([i,j])
print(lst_of_idx)














'''  given code is dummy code : no use  '''
# for i in range(n):
#     for j in range(n):
#         temp = []
#         if(sum(given_lst[i],given_lst[j]==sum) and i != j):
#             temp.append(i,j)
#         lst_of_idx.append(temp)
# print(lst_of_idx)