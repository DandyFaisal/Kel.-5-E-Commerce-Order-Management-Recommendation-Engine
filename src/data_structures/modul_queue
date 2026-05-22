from typing import Optional

# Node untuk Linked List
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None

class Queue:
    """FIFO Queue berbasis Singly Linked List."""
    def __init__(self):
        self.head: Optional[LLNode] = None
        self.tail: Optional[LLNode] = None
        self._size: int = 0

    def enqueue(self, data) -> None:
        """Big-O: O(1) sisip di tail."""
        # TODO: implementasikan
        pass

    def dequeue(self):
        """Big-O: O(1) ambil dari head."""
        # TODO: implementasikan
        pass

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size
