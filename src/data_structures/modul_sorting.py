from typing import Optional
from models import Order

class OrderNode:
    def __init__(self, order: Order):
        self.order = order
        self.next: Optional['OrderNode'] = None

def bubble_sort_by_total_harga_desc(head: Optional[OrderNode]) -> Optional[OrderNode]:
    # Implementasi dari kode asli (dipindahkan)
    if head is None:
        return None
    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next:
            if current.order.total_harga < current.next.order.total_harga:
                current.order, current.next.order = current.next.order, current.order
                swapped = True
            current = current.next
    return head

def insertion_sort_by_waktu_pesan_asc(head: Optional[OrderNode]) -> Optional[OrderNode]:
    if head is None or head.next is None:
        return head
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = _sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head

def _sorted_insert(head: Optional[OrderNode], new_node: OrderNode) -> OrderNode:
    if head is None or new_node.order.waktu_pesan < head.order.waktu_pesan:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.order.waktu_pesan < new_node.order.waktu_pesan:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
