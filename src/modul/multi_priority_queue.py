from typing import Optional
from model import Order

# ── Node Linked List ─────────────────────────────────────────
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None

# ── Queue berbasis Linked List ───────────────────────────────
class Queue:

    def __init__(self):
        self.head: Optional[LLNode] = None
        self.tail: Optional[LLNode] = None
        self._size: int = 0

    def enqueue(self, data) -> None:
        new_node = LLNode(data)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self._size += 1

    def dequeue(self):

        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next

        self._size -= 1

        if self.is_empty():
            self.tail = None

        return data

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def remove_by_condition(self, predicate) -> bool:

        prev = None
        current = self.head

        while current:

            if predicate(current.data):

                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                if current is self.tail:
                    self.tail = prev

                self._size -= 1
                return True

            prev = current
            current = current.next

        return False
