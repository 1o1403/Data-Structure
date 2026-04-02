class Node :
    def __init__ (self, data) :
        self.data = data
        self.next = None


# 연결 리스트로 스택 구현 시, head pointer를 top으로 사용한다.

class LinkedListStack :
    def __init__ (self) :
        self.top = None
        self.count = 0




    def push (self, value) :
        new_node = Node (value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1




    def pop (self) :
        if self.top.is_empty () :
            raise IndexError ("빈 스택입니다")
        
        value = self.top.data
        self.top = self.top.next
        self.count -= 1
        return value
    



    def peek (self) :
        if self.top.is_empty():
            raise IndexError ("빈 스택입니다")
        
        return self.top.data
    


    def is_empty (self) :
        return self.top is None
    



    def size (self) :
        return self.count
    

