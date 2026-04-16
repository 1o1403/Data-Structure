class ArrayCircularQueue:
    def __init__ (self, capacity):
        if capacity <= 1:
            raise ValueError("Capacity는 2 이상이어야 합니다") # 원형 큐는 하나는 메모리를 낭비하므로 최소 2 이상의 capacity가 필요함
        
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.capacity = capacity


    def is_empty(self):
        return self.front == self.rear
    


    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    


    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("큐가 가득 찼습니다")
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value

    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("큐가 비어 있습니다")
        
        self.front = (self.front + 1) % self.capacity
        return self.items[self.front]
    


    def peek(self):
        if self.is_empty():
            raise IndexError("큐가 비어 있습니다")
        
        return self.items[(self.front + 1) % self.capacity]
    


    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    