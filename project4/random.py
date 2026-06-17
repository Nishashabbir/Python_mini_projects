


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
# help me prepare for these questions in my lab assigment and exam : Queue using deque : code demonstrates enqueue dequeue operations using collections deque 

from collections import deque 

class Queue:
    def __init__(self):
        self.q=deque()
    def enqueue(self, value):
        self.q.append(value)
        print("value appended ")
    def dequeue(self):
        if self.isempty():
            print("it is already empty ")

        else:
            removed=self.q.popleft()
            print("remvoed : " , removed)
            return removed
    def isempty(self):
        return len(self.q)==0
    def display(self):
        print("Queue : " , list(self.q))

q=Queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.dequeue()



