from src.Chapter5Queues.Implementaions.LinkedList import Queue
import pytest

q = Queue()


def rear():
    return q.rear()


def head():
    return q.head()


en = q.enqueue
dq = q.dequeue


class TestQueue:
    def test_Enqueue(self):
        assert head() == None
        assert rear() == None
        for i in range(4):
            en(i)

        assert q.size() == 4


    def test_dequeue(self):
        for i in range(4):
            en(i)
            print(rear())
        assert q.size() == 4
        assert head() == 0
        assert rear() == 3
        assert dq() == 0
        assert q.size() == 3
        assert dq() == 1
