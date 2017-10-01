'''
Created on Oct 21, 2016

@author: www
'''



"""
import sys
lists=[1,2,3,4]
it = iter(lists) # this builds an iterator object
print (next(it)) #prints next available element in iterator
#Iterator object can be traversed using regular for statement
#!usr//bin/python3
for x in it:
    print (x, end=" ")
#or using next() function
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit() #you have to import sys module for this
 """
#!usr//bin/python3
import sys
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object

while True:
    try:
        print (next(f), end=" ")    
    except StopIteration:
        sys.exit()