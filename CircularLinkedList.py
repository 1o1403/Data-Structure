class Node:
    def __init__ (self, data=0) :
        self.data = data
        self.next = None



class CircularLinkedList:
    def __init__ (self):
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    

    #index 위치의 노드 반환
    def __node_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("인덱스 범위를 벗어났습니다.")
        
        current = self.tail.next #head부터 시작
        for _ in range(index):
            current = current.next
        return current
    

    #index 위치에 value 삽입: 0 <= index <= size
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("삽입 위치가 범위를 벗어났습니다.")
        
        new_node = Node(value)

        #빈 리스트인 경우
        if self.is_empty():
            new_node.next = new_node #자기 자신을 가리켜 원형 형성
            self.tail = new_node # 아직 self.tail = None이므로 새 노드를 tail로 설정까지 해줘야 함

        # 맨 앞 삽입
        elif index == 0:
            new_node.next = self.tail.next #새 노드가 기존 head를 가리킴
            self.tail.next = new_node #tail이 새 head를 가리키게 함

        # 맨 뒤 삽입
        elif index == self.size:
            new_node.next = self.tail.next #새 노드가 head를 가리킴
            self.tail.next = new_node #기존 tail 뒤에 새 노들 연결
            self.tail = new_node #새 노드를 새 tail로 갱신

        # 중간 삽입
        else:
            prev = self.__node_at( index - 1 ) #삽입 위치 바로 앞 노드
            new_node.next = prev.next 
            prev.next = new_node

        self.size += 1






    #index 위치에 노드 삭제(반환)
    def delete(self, index):
        if index < 0 or index >=self.size:
            raise IndexError("삭제 위치가 범위를 벗어났습니다.")
        
        #노드가 1개 뿐인 경우
        if self.size == 1:
            data = self.tail.data
            self.tail = None
            self.size = 0
            return data
        
        # 맨 앞 삭제
        if index == 0:
            head = self.tail.next 
            data = head.data
            self.tail.next = head.next  #두 번째 노드를 새 head로 만듦
            self.size -= 1
            return data
        
        # 중간 또는 맨 뒤 삭제
        prev = self.__node_at( index - 1 ) 
        target = prev.next
        data = target.data
        prev.next = target.next

        #삭제 대상이 tail이면 tail 갱신
        if target == self.tail:
            self.tail = prev #대입연산자: A = B는 B가 가리키고 있는 대상을 A도 가리키게 만들라.
        
        self.size -= 1
        return data
    




    # value 탐색: 있으면 index, 없으면 return -1
    def search(self, value) :
        if self.is_empty() :
            return -1
        
        current = self.tail.next #head부터 시작
        for index in range(self.size) : #원형리스트는 사이즈 크기로 for문을 돌려야 한다. 
            if current.data == value :
                return index
            current = current.next
        
        return -1
    
    



    #순회 출력
    def traverse(self) :
        if self.is_empty() :
            print("Empty")
            return
        
        current = self.tail.next #head부터 시작
        for _ in range(self.size) :
            print(current.data, end="  ->  ")
            current = current.next
        print(" (다시 head) ")




# 리스트 뒤집기
    def reverse(self) :
        if self.is_empty() :
            return

        old_head = self.tail.next #기존 head 저장
        prev = self.tail
        current = old_head

        for _ in range(self.size) :
            next_node = current.next #current의 원래 다음 노드를 먼저 저장
            current.next = prev      #current가 가리키는 방향을 반대로 바꿈

            #prev와 current를 한 칸씩 앞으로 이동
            prev = current
            current = next_node

        #기존 head가 뒤집힌 후 새 tail이 됨
        self.tail = old_head


