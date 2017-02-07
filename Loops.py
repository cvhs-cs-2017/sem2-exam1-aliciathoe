"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""
'''
x = 0

while x <= 100:
    print (x)
    x = x + 5


'''

"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""

def doubletriple(v):
    if v % 2 == 0:
        v = v * 3
    elif v % 2 == 1:
        v = v * 2
    else:
        v = v
    return v

print(doubletriple(1))
