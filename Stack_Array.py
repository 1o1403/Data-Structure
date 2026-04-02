class ArrayStack :
    def __init__ (self, capacity) :           # 배열은 고정 크기를 가지므로, capacity를 매개변수로 받음
        if capacity <= 0 :
            raise ValueError ("Capacity는 1 이상이어야 합니다.")
        
        self.items = [0] * capacity           # 스택의 요소를 저장할 배열
        self.top = -1                         # top이 인덱스 역할을 함, 초기값은 -1로 설정하여 스택이 비어 있음을 나타냄
        self.capacity = capacity


    
    def push(self, value) :
        if self.is_full() :
            raise OverflowError ("Stack이 가득 찼습니다.")
        
        self.top += 1                         # top은 항상 그 시점에 스택의 상단을 가리키도록 업데이트
        self.items[self.top] = value



    
    def pop(self) :
        if self.is_empty() :
            raise IndexError ("Stack이 비어 있습니다.")
        
        value = self.items[self.top]
        self.top -= 1
        return value
    



    def peek(self) :
        if self.is_empty() :
            raise IndexError ("Stack이 비어 있습니다.")
        
        return self.items[self.top]
    


    def is_empty(self) :
        return self.top == -1
    



    def is_full(self) :
        return self.top == self.capacity - 1
    



    def size(self) :
        return self.top + 1
    




