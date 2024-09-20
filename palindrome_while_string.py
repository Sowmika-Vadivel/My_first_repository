word = input("enter a word: ")
rev = ''
index = 0
while index < len(word):
    rev = word[index] + rev
    index+=1
print (f'{rev} is a reverse of WORD')
if word==rev:
    print(f'{word} is a palindrome')
else:
     print(f'{word} is not a palindrome')