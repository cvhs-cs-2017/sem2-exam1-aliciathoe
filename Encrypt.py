"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def RemoveVowels(x):
    newstring = ""
    x = x.lower()
    for ch in x:
        if ch is 'a':
            newstring = newstring + ''
        elif ch is 'e':
            newstring = newstring + ''
        elif ch is 'i':
            newstring = newstring + ''
        elif ch is 'o':
            newstring = newstring + ''
        elif ch is 'u':
            newstring = newstring + ''
        else:
            newstring = newstring + ch
    return newstring

NoVowels = RemoveVowels("Computer Science Makes the World go round but it doesn't make the world round itself!")
'''
print(NoVowels)

'''



"""Write an encryption code that you make up and run it for the variable NoVowels"""

def MyEncrypt(x):
    newstring = ""
    for ch in x:
        #print (ch, ord(ch))
        y = ord(ch) + 5
        newstring = newstring + chr(y)
    return newstring

print(MyEncrypt(NoVowels))
