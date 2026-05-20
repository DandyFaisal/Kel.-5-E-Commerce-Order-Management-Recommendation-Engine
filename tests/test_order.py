import time

from main import Queue, Order

def test_order_enqueue():
    q = Queue()

    order = Order(
        1,
        "C001",
        "P001",
        1,
        1,
        500000,
        time.time()
    )

    q.enqueue(order)

    hasil = q.dequeue()

    assert hasil.order_id == 1
    assert hasil.pelanggan == "C001"
    assert hasil.produk_kode == "P001"