# my_dict = {i:"dtr" for i in range(1, 10)}
# print(my_dict)
# temp = {
#     'key1' : {
#         "hi":1,
#         "he": {
#             "bye": 50
#         }
#     },
#     'key2':"end"
# }

# for i,j in enumerate(temp.items()):
#     print(j)

john= {"name":"John Doe","age":15}
dipa= dict(john)
dipa.update({"name":"Dipa Chiniya"})
# print(john,dipa)

# NOTE : Dictionary's copy() and dict() method actually make new individual copy of dictionary,(not assigning ref)

''' DOCSTRING :

here is the task of this file,
we have students named dictionary and now we want that 
every student has marks dictionary
we use loop and count result then store result as 
"name" : "percentage" 
'''

marks_of_dipa = {"maths":90,"phy":94, "che":78, "eng":45,"sanskrit":98}
marks_of_john = {"maths":89,"phy":86, "che":64, "eng":65,"sanskrit":80}
dipa.update({"marks":marks_of_dipa})
john.update({"marks":marks_of_john})
# print(dipa,john) 
list_of_student = [dipa,john]
# now looping statement where we calculate and store the result
result = {}
for i in list_of_student:
    for k,v in i.items():
        if k == "marks":
            name = i["name"]
            # print(i["name"],v) #debug point
            total = 0
            for j in v.values() :
                total += j
            # print(total) # debug point
            result[name] = total/5
print(result)