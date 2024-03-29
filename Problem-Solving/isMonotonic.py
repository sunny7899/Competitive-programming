      

# Monotonic means array in increasing or decreasing order 

def isMonotonic(A):  

    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or 

            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))  

   

A = [3, 4, 5, 6]  

print(isMonotonic(A)) 

# All elements of list are true
l = [4, 5, 1]
print(all(l))
  
# All elements of list are false
l = [0, 0, False]
print(all(l))