character = input("enter a character:")
if character.isalpha() and len(character)==1:
    if character in 'aeiouAEIOU':
        a=[]
        a[0]=character
        print (f"{a} is vowel")
    else :
        print(f"{ord(character)} is a consonant")

else: 
    print("invalid input")


    
  