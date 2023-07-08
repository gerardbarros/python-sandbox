# Heaps - find min and max of set of vals frequently
import heapq

# under the hood, they are created with arr
minHeap = []
heapq.heappush(minHeap, 3) # by default they are minHeaps
heapq.heappush(minHeap, 2) # by default they are minHeaps
heapq.heappush(minHeap, 4) # by default they are minHeaps

# To get min value, it will always be at index 0
print(minHeap[0])

# To loop while len is not 0, we can pop vals from heap
while len(minHeap):
    print(heapq.heappop(minHeap)) #minheal will show from small to large

# No max heaps but can do this, multiply each value we push by -1 and after pop the val we mult by -1 to negate original -1
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
# max will always be index 0
print(-1 * maxHeap[0])

# By popping each val and * -1, we confirm they are listed from big to small
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


# if have init set of vals to build heap, can do in linear time by using heapify (build heap)
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
# if not empty
while arr:
    print(heapq.heappop(arr))