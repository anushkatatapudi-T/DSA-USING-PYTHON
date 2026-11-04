queue =[]
def enqueue():
    n=int(input("Enter a number:"))
    queue.append(n)
    print(n,"is added to queue!")
def dequeue():
    if not queue:
        print("")
    else :
        e = queue.pop(0)
        print("Removed element is : ",e)
def display():
    print(queue)
while True:
    n1 = int(input("Enter your choice(1.add 2.remove 3.show 4.exit):"))
    if n1 == 1:
        enqueue()
    elif n1 == 2:
        dequeue()
    elif n1 == 3:
        display()
    else :
        print("Enter the correct operation")

import collections
q = collections.deque()
q.appendleft(10)
q.appendleft(30)
q.appendleft(50)
q.pop()
print(q)

q = collections.deque()
q.append(206)
q.append(202)
q.append(220)
q.popleft()
print(q)

import queue
q = queue.Queue()
q.put(3)
q.put(6)
q.put(9)
print(q.get())