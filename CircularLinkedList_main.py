from CircularLinkedList import CircularLinkedList

circle = CircularLinkedList()
circle.insert(0, 10)
circle.insert(1, 20)
circle.insert(2, 30)
circle.traverse() 

circle.delete(2)
circle.traverse()

circle.insert(0,30)
circle.traverse()

circle.reverse()
circle.traverse()