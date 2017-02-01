"""Define a function that will take a parameter, n, and triple it and return
the result"""

def Triple(n):
    x = n * 3
    return x

print(Triple(7))

"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """
print ('Enter a number to triple it.')

print(Triple(int(input())))
