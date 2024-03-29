'''
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

You are given a string
.
Your task is to find out if the string

contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string

.

Constraints

Output Format

In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if

has any uppercase characters. Otherwise, print False.

Sample Input

qA2

Sample Output

True
True
True
True
True

'''

# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

s = input()
v=False
for n in s:    
    if n.isalnum():
        v=True
print(v)
print ('ab123'.isalnum()) # True
print ('ab123#'.isalnum()) # False
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

v=False
for n in s:  
    if n.isalpha():
        v=True
print(v)
print ('abcD'.isalpha()) # True
print ('abcd1'.isalpha()) # False

# This method checks if all the characters of a string are digits (0-9).

v=False
for n in s:  
    if n.isdigit():
        v=True
print(v)
print ('1234'.isdigit()) # True
print ('123edsd'.isdigit()) # False
# This method checks if all the characters of a string are lowercase characters (a-z).

v=False
for n in s:  
    if n.islower():
        v=True
print(v)
print ('abcd123#'.islower()) # True
print ('Abcd123#'.islower()) # False

# This method checks if all the characters of a string are uppercase characters (A-Z).

v=False
for n in s:  
    if n.isupper():
        v=True
print(v)

print ('ABCD123#'.isupper()) # True
print ('Abcd123#'.isupper()) # False