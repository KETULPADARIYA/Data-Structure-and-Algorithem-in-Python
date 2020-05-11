class Queue:
    def __init__(self, limit=5):
        self.head = -1
        self.queue = []
        self.rear = -1
        self.limit = limit

    def enqueue(self, data):
        if self.rear + 1 == self.limit:
            print('Overflow')
            self.reset()
        if self.head == -1:
            self.rear = self.head = 0
        else:
            self.rear += 1
        self.queue.append(data)

    def dequeue(self):
        if self.rear + 1 == 0:
            print('Underflow')
            return None
        self.rear -= 1
        return self.queue.pop()

    def IsEmpty(self):
        return True if self.rear == 0 else False

    def peek(self):
        return self.queue[self.rear]

    def size(self):
        return self.rear + 1

    def reset(self):
        self.limit *= 2