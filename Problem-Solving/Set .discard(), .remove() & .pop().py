'''
Task

You have a non-empty set
, and you have to execute commands given in

lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer
, the number of elements in the set .
The second line contains space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next

lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints


Output Format

Print the sum of the elements of set

on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4

Explanation

After completing these
operations on the set, we get set. Hence, the sum is

.

Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.
'''

n = int(input())
s = set(map(int, input().split()))
inst=int(input())
for i in range(inst):
    ist=input()
    if ist.startswith('pop'):
        s.pop()
    elif ist.startswith('remove'):
        s.remove(int(ist.split()[-1]))
    elif ist.startswith('discard'):
        s.discard(int(ist.split()[-1]))
    else:
        pass
print(sum(s))

# set usage
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] 
for f in (set(basket)): 
   print(f) 

# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
s = set([1])
print (s.pop()) # 1
print (s) # set([])
print (s.pop()) # KeyError: pop from an empty set

# REMOVING ITEMS

# Both the discard() and remove() functions take a single value as an argument and removes that value from the set. If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print (s) # set([1, 2, 3, 4, 6, 7, 8, 9])
print (s.remove(4)) # None
print (s) # set([1, 2, 3, 6, 7, 8, 9])
s.remove(0) # KeyError: 0


s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.discard(5)
print (s) # set([1, 2, 3, 4, 6, 7, 8, 9])
print (s.discard(4)) # None
print (s) # set([1, 2, 3, 6, 7, 8, 9])
s.discard(0)
print (s) # set([1, 2, 3, 6, 7, 8, 9])


