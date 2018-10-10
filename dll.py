def __init__(self):
	pass
class DoubleLinkedList(object):
    class Item(object):
        def __init__(self, prev, elem, next):
            self.prev = prev
            self.elem = elem
            self.next = next

    def __init__(self):
        self.__NULL__ = 0
        self.head = self.__NULL__
        self.tail = self.__NULL__
        self.size = 0

    def push(self, elem):
        self.tail = self.Item(self.tail, elem, self.__NULL__)
        if self.head == self.__NULL__:
            self.head = self.tail
        else:
            self.tail.prev.next = self.tail
        self.size = self.size + 1

    def pop(self):
        if self.tail == self.__NULL__:
            raise Exception("List is empty")
        else:
            tmp = self.tail.elem
            self.tail = self.tail.prev
            if self.tail == self.__NULL__:
                self.head = self.__NULL__
            else:
                self.tail.next = self.__NULL__
            self.size = self.size - 1
            return tmp

    def unshift(self, elem):
        self.head = self.Item(self.__NULL__, elem, self.head)
        if self.tail == self.__NULL__:
            self.tail = self.head
        else:
            self.head.next.prev = self.head
        self.size = self.size + 1

    def shift(self):
        if self.head == self.__NULL__:
            raise Exception("List is empty")
        else:
            tmp = self.head.elem
            self.head = self.head.next
            if self.head == self.__NULL__:
                self.tail = self.__NULL__
            else:
                self.head.prev = self.__NULL__
            self.size = self.size - 1
            return tmp

    def len(self):
        return self.size

    def delete(self, elem):
        tmp = self.head
        for i in range(self.size):
            if tmp.elem == elem:
                if tmp.prev != self.__NULL__:
                    tmp.prev.next = tmp.next
                else:
                    self.head = tmp.next
                if tmp.next != self.__NULL__:
                    tmp.next.prev = tmp.prev
                else:
                    self.tail = tmp.prev
                self.size = self.size - 1
                break
            else:
                tmp = tmp.next

    def contains(self, elem):
        tmp = self.head
        for i in range(self.size):
            if tmp.elem == elem:
                return True
                break
            else:
                tmp = tmp.next
        return False

    def first(self):
        if self.head == self.__NULL__:
            raise Exception("List is empty")
        else:
            return self.head.elem

    def last(self):
        if self.tail == self.__NULL__:
            raise Exception("List is empty")
        else:
            return self.tail.elem
