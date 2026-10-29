from collections import deque

task = deque(["Task1","Task2","Task3"])

while task:
    print("Executing:", task.popleft())

print("All task completed.")
