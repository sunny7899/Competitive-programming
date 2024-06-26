

'''
Objective
Today, we're learning and practicing an algorithmic concept called Recursion. 

Recursive Method for Calculating Factorial
Task
Write a factorial function that takes a positive integer,
as a parameter and prints the result of (
factorial).
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of
.
Input Format
A single integer,
(the argument to pass to factorial).

Sample Input
3

Sample Output
6

Explanation
Consider the following steps:
From steps and , we can say ; then when we apply the value from to step , we get . Thus, we print as our answer.
'''

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

n = int(input())
result = factorial(n)
print(result)

def factWithoutRecursion(n):
    temp = 1
    for i in range(n, 0, -1):
        temp = temp * i
    return temp
a = factWithoutRecursion(5) 
print(a) 


 
