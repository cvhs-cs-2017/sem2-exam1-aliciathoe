"""Use the range function to print the numbers from 40 to 1 (backwards)"""
'''
for  i in range(40 , 0 , -1):
    print (i)
'''
"""Repeat the exercise but count by 5's"""
'''
for i in range(40 , 0 , -5):
    print (i)
'''
"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""

print ("Enter a number to find its multiples.")
n = int(input())
m = n

for i in range(m , 0 , -1):
    if n % m == 0:
        print (m)
    m = m - 1
