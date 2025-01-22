'''
str = 'What is Lorem Ip
sum Lorem Ipsum is simpl
y dummy text of the print
ing and typesetting indust
ry Lorem Ipsum has been th
e industry's standard dummy 
text ever since the 1500s wh
en an unknown printer took a 
galley 

Of type and scrambled it to make a type specimen book it has? '



	​=> find total occurance of each letter = ‘aeiou’
 '''

count = 0
myStr = '''What is Lorem Ip
sum Lorem Ipsum is simpl
y dummy text of the print
ing and typesetting indust
ry Lorem Ipsum has been th
e industry's standard dummy 
text ever since the 1500s wh
en an unknown printer took a 
galley 
'''

count = sum([1 for i in myStr if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ]) #string comprehension    
print(count)

