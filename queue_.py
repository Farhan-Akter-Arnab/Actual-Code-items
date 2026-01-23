ar = [0 for _ in range(10)]
n = 10
front, rear = -1, -1
def enqueue(item):
    global n, rear, front
    if rear == n - 1:
        print("Overflow!")
        return
    if front == -1 and rear == -1:
        front, rear = 0, 0
    else:
        rear += 1
    ar[rear] = item
    print("Element inserted!")
def dequeue():
    global n, rear, front
    if front == -1 and rear == -1:
        print("Underflow!")
        return
    item = ar[front]
    print("Element deleted from queue is:", item)
    if front == rear:
        front, rear = -1, -1
    else:
        front += 1
def display():
    global rear, front
    if front == -1 and rear == -1:
        print("Queue is empty")
        return
    print("Elements in the queue are:", end=" ")
    for i in range(front, rear + 1):
        print(ar[i], end=" ")
    print()
def fronte():
    global front
    if front == -1 and rear == -1:
        print("Queue is empty")
        return
    print("Front element is:", ar[front])
print("1: Inserting element to queue (Enqueue)")
print("2: Deleting element from queue (Dequeue)")
print("3: Displaying elements of queue")
print("4: Displaying front element of queue")
print("5: Exit")
condition = True
while condition:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to be inserted: "))
        enqueue(item)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        fronte()
    elif choice == 5:
        print("Exiting...")
        condition = False
    else:
        print("Invalid choice! Please try again.")