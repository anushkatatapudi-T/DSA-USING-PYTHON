# stack = []
# def push():
#     if len(stack)==n:
#         print("List is full")
#     else:
#         element = int(input("Enter element to add : "))
#         stack.append(element)
#         print("Your stack is :",stack)
# def pop_element():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("Element is removed:",e)
# n = int(input("Enter your limit:"))
# while True:
#     print("Select the operation:\n1.Push\n2.Pop\n3.Quit")
#     n = int(input("Enter ur selection:"))
#     if n == 1:
#         push()
#     elif n ==2 :
#         pop_element()
#     elif n == 3 :
#         print("thankyou for using")
#         break
#     else :
#         print("Please enter correct choice")

import collections
s = collections.deque()
s.append(10)
s.append(30)
s.pop()
print(s)
import queue
s1=queue.LifoQueue()
s1.put(20)
s1.put(30)
print(s1.put(15))