#separate the uppercase letters in upper and lowercase letters in lower
 
word = input("enter a word :")
lower =''
upper=''
index = 0
while index < len(word):
    char = word[index]
    index += 1
    if char.isupper():
        upper += char
    else :
        lower += char
print (f"{upper} are upppercase letters in the word")
print (f"{lower} are lowercase letters in  the word")

