


# import hashlib
# message=input("Enter the username :  ")
# print("WELCOME!")
# message1=input("Enter the message ")
# hash1=hashlib.sha256(message1.encode()).hexdigest()
# print("This is the encoded message/signature: " , hash1)

# # verify it 
# message2=input("Enter the message to verify : ")
# hash2=hashlib.sha256(message2.encode()).hexdigest()

# if hash1==hash2:
#     print("The message is verified! ")
# else:
#     print("The message is not verified yet ! ")








# simple xor encryption and decryption 

# key=12
# message= input("Enter your message : " )


# Encryption 

# ciphertext=""

# for char in message:
#     ciphertext+=chr(ord(char)^ key)
# print("Encryption message : " , ciphertext)



# # decryption 

# plaintext=""

# for char in ciphertext:
#     plaintext+=chr(ord(char)^key)
# print("Decryption : " , plaintext)




















# Q-1
# Queue using deque : code demonstrates enqueue dequeue operations using collections deque 


# solution : 
# A Queue follows FIFO (First In First Out):

# Insert → enqueue (rear)
# Remove → dequeue (front)
# Python’s collections.deque is perfect because:
# Fast insertion/removal from both ends → O(1)

# from collections import deque 

# class Queue:
#     def __init__(self):
#         self.q=deque()
#     def enqueue(self, value):
#         self.q.append(value)
#         print("value appended ")
#     def dequeue(self):
#         if self.isempty():
#             print("it is already empty ")

#         else:
#             removed=self.q.popleft()
#             print("remvoed : " , removed)
#             return removed
#     def isempty(self):
#         return len(self.q)==0
#     def display(self):
#         print("Queue : " , list(self.q))

# q=Queue()
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.display()
# q.dequeue()
# q.dequeue()





    














# Q-2 

# NumPy supports vectorized operations, meaning:
# You don’t need loops
# Operations apply to all elements automatically


# import numpy as np 

# arr=np.array([1,2,3,4,5])
# result= arr*2

# print("original array : " , arr)
# print("Modified array : " , result)





# Q-3 
# from collections import deque

# # Graph (Adjacency List)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

# def bfs(start):
#     visited = set()
#     queue = deque()

#     queue.append(start)
#     visited.add(start)

#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

# # Start BFS from A
# bfs('A')












# second try 

# from collections import deque

# graph={
#     'A' : ['B' , 'C'] , 
#     'B' : ['D' , 'E'] , 
#     'C' : ['F'] , 
#     'D' : [] , 
#     'E' : [] , 
#     'F' : [] , 
# }

# f should be there in both 

# lets create the bfs function 

# def bfs(start):
#     visited=set() #for unique values 
#     queue=deque()  #for empty queue 

#     # what to do with the argument now ? 
#     queue.append(start)
#     visited.add(start)

#     # now run a loop until the queue is empty 
#     while queue:
#         node = queue.popleft() #we will use it later on 
#         print(node )

#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 queue.append(neighbour)
#                 visited.add(neighbour)

# bfs('A')






# Q-4 
# import pandas as pd

# # Create data
# data = {
#     'Name': ['Ali', 'Sara', 'Ahmed', 'Ayesha'],
#     'Age': [20, 22, 19, 21]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Display DataFrame
# print("DataFrame:")
# print(df)

# # Summary statistics
# print("\nSummary using describe():")
# print(df.describe())















# import pandas as pd 

# data={
#     'Name' : ['Ali ' , 'Sara' , 'Sana ' , 'Ahmad'] ,
#     'Age' : [20 , 23 , 25 , 26 ]
# } 


# # create data frame 

# df=pd.DataFrame(data)

# # display 
# print(df)

# print(df.describe())


# ///////////////////////////////


# insertion in binary search tree 
class Node: 
    def __init__(self, value):
        self.root=value
        self.right=None
        self.left=None

def insert(root , value):
    if root is None: 
        root=Node(value)
    if value < root.value:
        root.left=insert(root.left , value)
    else:
        root.right=insert(root.right , value)
    return root

# example usage 
root=None
values=[10 , 20 , 40 , 60 , 80]
for v in values: 
    insert(root , v )


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def insert(root, value):
#     # If tree is empty
#     if root is None:
#         return Node(value)

#     # If value is smaller → go left
#     if value < root.value:
#         root.left = insert(root.left, value)

#     # If value is greater → go right
#     else:
#         root.right = insert(root.right, value)

#     return root


# # Example usage
# root = None
# values = [50, 30, 70, 20, 40, 60, 80]

# for v in values:
#     root = insert(root, v)           


# ///////////////////////////////////////////////////////////////
