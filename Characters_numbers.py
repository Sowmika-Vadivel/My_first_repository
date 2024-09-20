# Separate the characters and numbers and symbols from the user entered srting


word = input("enter a string :")
num =''
str= ''
symbol=''
index = 0
while index < (len(word)):
    i = word[index]
    index += 1
    if i.isalpha():
        str += i
    elif i.isnumeric():
        num += i
    else:
        symbol += i

print (f"{num} are numbers")
print (f"{str} are the characters")
print (f"{symbol} are the symbols")

    

  