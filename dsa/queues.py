# Queues are double ended by default
from collections import deque

queue = deque()

# append adds values to right side
queue.append(0)
queue.append(1)
queue.append(2)
print(queue)

# remove from left and done in constant time
queue.popleft()
print(queue)

# can add to left
queue.appendleft(5)
print(queue)

# remove from right
queue.pop()
print(queue)