from src.Chapter3LinkedList.LinkedList.NodeSingleLinkedList import Node


class Queue:
    def __init__(self):
        self.size_ = 0
        self.head_ = None
        self.rear_ = None

    def enqueue(self, data):

        temp = Node(data)
        if self.head_ == None:
            self.head_ = self.rear_ = temp

        else:
            self.rear_.setNext(temp)
            self.rear_ = temp
        self.size_ += 1

    def dequeue(self):
        if self.rear_ == None:
            print('Underflow')
            return None
        node = self.head_
        self.size_ -= 1
        self.head_ = self.head_.getNext()
        self.head_.setNext(node.getNext())
        return node.getData()

    def IsEmpty(self):
        return True if self.rear_ == 0 else False

    def peek(self):
        return self.rear_.getNext()

    def size(self):
        return self.size_

    def head(self):
        return self.head_.getData() if self.head_ else None

    def rear(self):
        return self.rear_.getData() if self.rear_ else None


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    for i in range(5):
        q.enqueue(i)
        print('head',q.head())
        print('rear',q.rear())