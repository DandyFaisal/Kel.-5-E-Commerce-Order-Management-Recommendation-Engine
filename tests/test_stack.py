from main import Stack

def test_push():
    s = Stack(kapasitas=5)

    assert s.push(1) == True
    assert s.push(2) == True

def test_pop():
    s = Stack(kapasitas=5)

    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_overflow():
    s = Stack(kapasitas=2)

    s.push(1)
    s.push(2)

    assert s.push(3) == False