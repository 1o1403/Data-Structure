class Node:
    def __init__ (self, data=0) :
        self.data = data
        self.next = None



class LinkedList:
    def __init__ (self) :
        self.header = Node()  #header node - 실제 데이터를 가지고 있지 않음.
        self.size = 0



    # index 위치에 value를 삽입하는 메소드
    def insert (self, index, value) :
        # 삽입 가능 여부 판단: 0 <= index <= size 이면 삽입 가능
        if index < 0 or index > self.size :
            raise IndexError("삽입 위치가 범위를 벗어났습니다.")
        
        #삽입 위치 바로 앞 노드 찾기 
        prev = self.header
        for _ in range(index) :
            prev = prev.next

        #새 노드 생성 후, 끼워 넣기
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1



    # index 위치의 노드를 삭제(=반환)하는 메소드
    def delete (self, index) :
        # 삭제 가능 여부 판단: 0 <= index < size 이면 삭제 가능
        if index < 0 or index >= self.size :
            raise IndexError("삭제 위치가 범위를 벗어났습니다.")
        
        # 삭제할 위치 바로 앞 노드 찾기
        prev = self.header
        for _ in range(index) :
            prev = prev.next

        target = prev.next
        prev.next = target.next
        self.size -= 1

        return target.data
    



    # 탐색: value 값을 찾아서, 있으면 인덱스 반환, 없으면 -1 반환
    def search(self, value) :
        current = self.header.next
        index = 0

        while current is not None :
            if current.data == value :
                return index
            current = current.next
            index += 1
        
        return -1 




    # 순회: 연결 리스트를 처음부터 끝까지 순회하면서 출력하는 메소드
    def traverse(self) :
        current = self.header.next

        while current is not None :
            print(current.data, end="  ->  ")
            current = current.next

        print("None")



    
    # 리스트를 뒤집기
    def reverse(self) :
        prev = None
        current = self.header.next

        while current is not None :
            next_node = current.next   # 다음 노드를 미리 저장
            current.next = prev        # 링크 방향 뒤집기
            prev = current             # prev 한 칸 이동
            current = next_node        # current 한 칸 이동
        
        self.header.next = prev