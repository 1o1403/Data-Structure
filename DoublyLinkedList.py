class Node:
    def __init__(self, data=0) :
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__ (self):
        self.header = Node()    # 맨 앞 더미 노드
        self.trailer = Node()   # 맨 뒤 더미 노드

        self.header.next = self.trailer
        self.trailer.prev = self.header

        self.size = 0

    


    # index 위치의 실제 노드 반환
    def _get_node(self, index):
        if index < 0 or index >= self.size :
            raise IndexError("인덱스가 범위를 벗어났습니다.")
        
        #앞쪽이 더 가까우면 앞에서, 뒤쪽이 더 가까우면 뒤에서 탐색
        if index < self.size //2:
            current = self.header.next
            for _ in range(index) :
                current = current.next
        else:
            current = self.trailer.prev
            for _ in range(self.size - index - 1) :
                current = current.prev

        return current
    





    # index 위치에 value 값을 삽입
    def insert(self, index, value) :
        if index < 0 or index > self.size :
            raise IndexError("인덱스가 범위를 벗어났습니다.")
        
        new_node = Node(value)

    
        # 맨 뒤 삽입이면 trailer 앞에 넣는다.
        if index == self.size :
            next_node = self.trailer
        else : 
            next_node = self._get_node(index)
    
        prev_node = next_node.prev

        # prev_node <-> new_node <-> next_node 로 연결
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

        self.size += 1







    # index 위치의 실제 노드를 삭제하고 data 반환
    def delete(self, index) :
        target = self._get_node(index)

        prev_node = target.prev
        next_node = target.next

        # prev_node <-> next_node 로 다시 연결
        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

        # 삭제된 노드를 완전히 분리
        target.prev = None
        target.next = None

        return target.data
    





    # value 값을 찾아 인덱스 반환, 없으면 -1
    def search(self, value):
        current = self.header.next
        index = 0

        while current is not self.trailer :
            if current.data == value :
                return index
            current = current.next
            index += 1
        
        return -1
    




    # 정방향 순회 출력
    def traverse(self):
        current = self.header.next

        while current is not self.trailer :
            print(current.data, end=" <=> ")
            current = current.next

        print("None")




    # 역방향 순회 출력
    def reverse_traverse(self):
        current = self.trailer.prev

        while current is not self.header :
            print(current.data, end=" <=> ")
            current = current.prev

        print("None")

    




    # 리스트 전체 뒤집기
    def reverse(self):
        if self.size <= 1 :
            return         # 함수를 즉시 종료하고, None이라는 값을 반환하라는 뜻
        
        current = self.header.next
        old_first = current
        old_last = self.trailer.prev

        while current is not self.trailer :
            current.prev, current.next = current.next, current.prev
            current = current.prev  # 바뀐 prev는 원래 next였음

        self.header.next = old_last
        old_last.prev = self.header

        self.trailer.prev = old_first
        old_first.next = self.trailer











