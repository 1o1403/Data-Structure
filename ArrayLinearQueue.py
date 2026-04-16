class ArrayLinearQueue:
    def __init__ (self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity는 1 이상이어야 합니다.")
        
        self.items = [None] * capacity     # 공간 할당
        self.front = -1
        self.rear = -1
        self.capacity = capacity


    

    def is_empty(self):
        return self.front == -1
    



    def is_full(self):
        return self.rear == self.capacity - 1
    



    def enqueue(self, value):        # 큐에 데이터 추가
        if self.is_full():
            raise OverflowError("Queue가 가득 찼습니다.")
        
        if self.is_empty():          
            self.front = 0

        self.rear += 1
        self.items[self.rear] = value

    


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue가 비어 있습니다.")
        
        value = self.items[self.front]   # 삭제할 값은 나중에 반환할 것이므로 저장해 둠

        if self.front == self.rear:   # 큐에 하나의 요소만 있는 경우
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value
    
    

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue가 비어 있습니다.")
        
        return self.items[self.front]
    


    def size(self):
        if self.is_empty():
            return 0
        
        return self.rear - self.front + 1
    


