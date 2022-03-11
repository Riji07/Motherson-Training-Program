# Python program to
# demonstrate queue implementation
# using list
# Initializing a queue
queue = []
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(1))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty






# Python program to
# demonstrate queue implementation
# using collections.dequeue
from collections import deque
# Initializing a queue
q = deque()
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty





# Python program to
# demonstrate implementation of
# queue using queue module
from queue import Queue
# Initializing a queue
q = Queue(maxsize = 3)
# qsize() give the maxsize
# of the Queue
print(q.qsize())
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
# Return Boolean for Full
# Queue
print("\nFull: ", q.full())
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())






# Python code to demonstrate deque
from collections import deque
# Declaring deque
queue = deque(['name','age','DOB'])
print(queue)






# Python code to demonstrate working of
# append(), appendleft(), pop(), and popleft()
# importing "collections" for deque operations
import collections
# initializing deque
de = collections.deque([1,2,3])
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
# printing modified deque
print ("The deque after appending at right is : ")
print (de)
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
# printing modified deque
print ("The deque after appending at left is : ")
print (de)
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
# printing modified deque
print ("The deque after deleting from right is : ")
print (de)
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
# printing modified deque
print ("The deque after deleting from left is : ")
print (de)






# Python code to demonstrate working of
# insert(), index(), remove(), count()
# importing "collections" for deque operations
import collections
# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])
# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))
# using insert() to insert the value 3 at 5th position
de.insert(4,3)
# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)
# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))
# using remove() to remove the first occurrence of 3
de.remove(3)
# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)






# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()
# importing "collections" for deque operations
import collections
# initializing deque
de = collections.deque([1, 2, 3,])
# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])
# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)
# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([7,8,9])
# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)
# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)
# printing modified deque
print ("The deque after rotating deque is : ")
print (de)
# using reverse() to reverse the deque
de.reverse()
# printing modified deque
print ("The deque after reversing deque is : ")
print (de)







