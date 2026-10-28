from collections import deque

queue = deque(maxlen=5)

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print("Queue:",list(queue))

queue.popleft()
queue.append(60)

print("After Circular Operation:",list(queue))
