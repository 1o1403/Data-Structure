class Node:
    def __init__ (self, data = 0):
        self.data = data
        self.next = None   

class LinkedListQueue:
    def __init__ (self):
        self.front = None
        self.rear = None
        self.count = 0

    
    def is_empty (self):
        return self.front is None
    

    def enqueue (self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1


    
    def dequeue (self):
        if self.is_empty():
            raise Exception("빈 큐입니다.")
        
        value = self.front.data
        self.front = self.front.next
        self.count -= 1

        if self.front is None:
            self.rear = None

        return value
    


    def peek (self):
        if self.is_empty():
            raise Exception("빈 큐입니다.")
        
        return self.front.data




    def size (self):
        return self.count
    



