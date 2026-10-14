queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:",queue)

# Dequeue
item = queue.pop(2)
print("Deleted:",item)

print("Queue after deletion:",queue)
