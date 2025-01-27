# Reverse Only Vowels in a String

str = "python"
myVowels = []
chr = list(str)
def isVowel(str):
    if str in ['a','e','i','o','u']:
        return True
    else :
        return False
    
myVowels = [i for i in str if isVowel(i)]
for i in range(len(chr)):
    if(isVowel(chr[i])):
        tm = myVowels[len(myVowels)-1]
        chr[i] = tm
        myVowels.remove(tm)
        print(myVowels)
print(chr)