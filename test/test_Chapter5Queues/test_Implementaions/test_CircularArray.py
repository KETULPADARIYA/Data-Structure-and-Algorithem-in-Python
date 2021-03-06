from src.Chapter5Queues.Implementaions.CircularArray import Queue
import pytest

q = Queue()
queue = q.queue


def rear():
    return q.rear


def head():
    return q.head


en = q.enqueue
dq = q.dequeue


class TestQueue:
    def test_Enqueue(self):
        assert head() == -1
        assert rear() == -1
        for i in range(4):
            en(i)

        assert q.size() == 4


    def test_dequeue(self):
        for i in range(4):
            en(i)

        assert q.head == 0
        assert q.rear == 3
        assert dq() == 3
        assert q.size() == 3
        assert dq() == 2
