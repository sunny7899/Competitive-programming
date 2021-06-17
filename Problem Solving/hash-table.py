# Hashing/Heap Operations
# Hashing O(1) Operation,
# Priority Queue, MaxHeap/Min Heap,
# Heapify Operation, Find Medians,
# Merge Operation in O(Logn) using Heap

# Hash tables?
# Hash Table is a data structure which stores data in an associative manner. In this, data is stored in an array format, where each data value has its own unique index value.
# Use Hash Table for quick lookups
# stores elements in key-value pairs

# In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.

# When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.

# We can resolve the hash collision using .
# Collision resolution by chaining
# Open Addressing: Linear/Quadratic Probing and Double Hashing

def hash_key( key, m):
    return key % m


m = 7

# print(f'The hash value for 3 is {hash_key(3,m)}')
# print(f'The hash value for 2 is {hash_key(2,m)}')
# print(f'The hash value for 9 is {hash_key(9,m)}')
# print(f'The hash value for 11 is {hash_key(11,m)}')
# print(f'The hash value for 7 is {hash_key(7,m)}')


hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable, 'hashTable')

removeData(123)

print(hashTable, 'after removing 123')