import time

from main import (
    Order,
    bubble_sort_by_harga,
    insertion_sort_by_waktu
)

def test_bubble_sort_by_harga():
    orders = [
        Order(1, "C001", "P001", 1, 1, 10000, time.time()),
        Order(2, "C002", "P002", 1, 1, 50000, time.time()),
        Order(3, "C003", "P003", 1, 1, 30000, time.time())
    ]

    hasil = bubble_sort_by_harga(orders)

    assert hasil[0].total_harga == 50000
    assert hasil[1].total_harga == 30000
    assert hasil[2].total_harga == 10000

def test_insertion_sort_by_waktu():
    orders = [
        Order(1, "C001", "P001", 1, 1, 10000, 300),
        Order(2, "C002", "P002", 1, 1, 50000, 100),
        Order(3, "C003", "P003", 1, 1, 30000, 200)
    ]

    hasil = insertion_sort_by_waktu(orders)

    assert hasil[0].waktu_pesan == 100
    assert hasil[1].waktu_pesan == 200
    assert hasil[2].waktu_pesan == 300