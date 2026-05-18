#contoh saya pakai terminal
#ORDER C001 P012 REGULAR
#.
#.
#.
#ORDER C002 P021 REGULAR
#.
#.
#.
#rekomendasi ketiknya gimana?
import time, random
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

random.seed(99)

TIER = {'PREMIUM': 1, 'REGULAR': 2, 'ECONOMY': 3}
TIER_NAME = {v: k for k, v in TIER.items()}

@dataclass
class Produk:
    kode: str                 # P001-P100
    nama: str
    harga: float
    stok: int

@dataclass
class Order:
    order_id: int
    pelanggan: str            # C001-C050
    produk_kode: str
    tier: int                 # 1=PREMIUM, 2=REGULAR, 3=ECONOMY
    qty: int
    total_harga: float
    waktu_pesan: float        # time.time()

# ── Node Linked List ─────────────────────────────────────────
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None

# ── Queue berbasis Linked List ───────────────────────────────
class Queue:
    """FIFO Queue berbasis Singly Linked List."""
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
