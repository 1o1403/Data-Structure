from LinkedList import LinkedList

lst = LinkedList()
lst.insert(0,100)
lst.traverse()

lst.insert(0,10)
lst.insert(1,30)
lst.insert(3,20)
lst.traverse()
print("삭제: ", lst.delete(1))
lst.traverse()

lst.insert(0,1)
lst.insert(1,2)
lst.insert(2,3) 
lst.insert(3,4)

lst.traverse()
lst.reverse()
lst.traverse()