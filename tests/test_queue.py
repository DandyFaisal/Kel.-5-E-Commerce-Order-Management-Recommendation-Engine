from main import Queue

def test_enqueue():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)

    assert len(q) == 2

def test_dequeue():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)

    assert q.dequeue() == 10
    assert q.dequeue() == 20

def test_is_empty():
    q = Queue()

    assert q.is_empty() == True

    q.enqueue(1)

    assert q.is_empty() == False
