"""
Test suite untuk E-Commerce Order Management & Recommendation Engine
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import (
    Queue, Stack, Produk, Order, TIER, TIER_NAME,
    BSTKatalog, GraphRekomendasi, generate_produk,
    bubble_sort_by_harga, insertion_sort_by_waktu
)
import time
import pytest


def test_produk_creation():
    """Test Produk dataclass creation"""
    p = Produk("P001", "Laptop", 5000000, 10)
    assert p.kode == "P001"
    assert p.nama == "Laptop"
    assert p.harga == 5000000
    assert p.stok == 10


def test_order_creation():
    """Test Order dataclass creation"""
    o = Order(1, "Cust1", "P001", 1, 1, 5000000, time.time())
    assert o.order_id == 1
    assert o.pelanggan == "Cust1"
    assert o.tier == 1


def test_queue_operations():
    """Test Queue enqueue and dequeue"""
    q = Queue()
    assert q.is_empty()

    q.enqueue("item1")
    assert len(q) == 1

    q.enqueue("item2")
    assert len(q) == 2

    assert q.dequeue() == "item1"
    assert q.dequeue() == "item2"
    assert q.is_empty()


def test_stack_operations():
    """Test Stack push and pop"""
    s = Stack(kapasitas=5)
    assert s._size == 0

    s.push("item1")
    assert s._size == 1

    s.push("item2")
    assert s._size == 2

    assert s.pop() == "item2"
    assert s.pop() == "item1"
    assert s._size == 0


def test_bst_insert_search():
    """Test BST insert and search operations"""
    bst = BSTKatalog()

    p1 = Produk("P001", "Laptop", 5000000, 10)
    p2 = Produk("P002", "Mouse", 200000, 50)

    bst.insert(p1)
    bst.insert(p2)

    found = bst.search("P001")
    assert found is not None
    assert found.nama == "Laptop"

    not_found = bst.search("P999")
    assert not_found is None


def test_bst_update_stok():
    """Test BST update stock"""
    bst = BSTKatalog()
    p = Produk("P001", "Laptop", 5000000, 10)
    bst.insert(p)

    assert bst.update_stok("P001", 5)
    updated = bst.search("P001")
    assert updated.stok == 15


def test_graph_rekomendasi():
    """Test Graph recommendation"""
    graph = GraphRekomendasi()

    graph.add_copurchase("P001", "P002")
    graph.add_copurchase("P002", "P003")

    recom = graph.rekomendasi("P001", max_hop=2)
    assert "P002" in recom
    assert "P003" in recom


def test_generate_produk():
    """Test product generation"""
    products = generate_produk(50)
    assert len(products) == 50
    assert all(isinstance(p, Produk) for p in products)


def test_bubble_sort():
    """Test bubble sort by harga"""
    now = time.time()
    orders = [
        Order(1, "C1", "P1", 1, 1, 1000, now),
        Order(2, "C2", "P2", 1, 1, 5000, now),
        Order(3, "C3", "P3", 1, 1, 3000, now),
    ]

    sorted_orders = bubble_sort_by_harga(orders)
    assert sorted_orders[0].total_harga == 5000
    assert sorted_orders[1].total_harga == 3000
    assert sorted_orders[2].total_harga == 1000


def test_insertion_sort():
    """Test insertion sort by waktu"""
    now = time.time()
    orders = [
        Order(1, "C1", "P1", 1, 1, 1000, now + 100),
        Order(2, "C2", "P2", 1, 1, 5000, now),
        Order(3, "C3", "P3", 1, 1, 3000, now + 50),
    ]

    sorted_orders = insertion_sort_by_waktu(orders)
    assert sorted_orders[0].waktu_pesan <= sorted_orders[1].waktu_pesan
    assert sorted_orders[1].waktu_pesan <= sorted_orders[2].waktu_pesan


def test_tier_constants():
    """Test TIER and TIER_NAME constants"""
    assert TIER['PREMIUM'] == 1
    assert TIER['REGULAR'] == 2
    assert TIER['ECONOMY'] == 3

    assert TIER_NAME[1] == 'PREMIUM'
    assert TIER_NAME[2] == 'REGULAR'
    assert TIER_NAME[3] == 'ECONOMY'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
