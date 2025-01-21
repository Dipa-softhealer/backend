# str1 = input("define your favorite string: ")

# temp = input("try to retype the string: ")
# if temp == str1 :
#     print("Yey you find it!Congrats...")
# else :
#     print("you missed!")
#     ch=""
#     while(ch !="q"):
#         temp=input("try again! : ")        
#         if(temp == str1) :
#             print("Yey you find it!Congrats...")
#             break      
#         ch = input("wanna Quit? :")
        


tempStr = input("type a string ")
myStr = ""
while(myStr != tempStr):
    myStr = input("re-type :")

else :
    print("Yey You did it!")