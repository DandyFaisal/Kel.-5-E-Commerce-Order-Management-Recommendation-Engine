from typing import Optional


class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None


class Stack:
    """LIFO Stack berbasis Singly Linked List."""
    def __init__(self, kapasitas=10):
        self.top: Optional[LLNode] = None
        self._size: int = 0
        self.kapasitas = kapasitas

    def push(self, data) -> bool:
        """Big-O: O(1). Kembalikan False jika kapasitas penuh."""
        if self._size >= self.kapasitas:
            return False
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        return True

    def pop(self):
        """Big-O: O(1). Hapus dan kembalikan data dari top."""
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size
