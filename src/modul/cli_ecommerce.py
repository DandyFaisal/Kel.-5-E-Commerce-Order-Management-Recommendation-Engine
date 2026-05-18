import time
import random

from typing import Dict, List

from models import *
from multi_priority_queue import Queue
from stack_riwayat import Stack
from bst_katalog import BSTKatalog
from graph_rekomendasi import GraphRekomendasi
from sorting_laporan import *

random.seed(99)

# ── Generator data awal ──────────────────────────────────────
def generate_produk(n=100) -> List[Produk]:

    nama_template = [
        'Laptop',
        'Mouse',
        'Keyboard',
        'Monitor',
        'Headset',
        'Webcam',
        'USB Hub',
        'Charger',
        'Kabel HDMI',
        'Speaker'
    ]

    produk_list = []

    for i in range(1, n + 1):

        kode = f'P{i:03d}'

        nama = f"{random.choice(nama_template)} Model-{i}"

        harga = round(
            random.uniform(50_000, 5_000_000),
            -3
        )

        stok = random.randint(0, 200)

        produk_list.append(
            Produk(kode, nama, harga, stok)
        )

    return produk_list


def main():

    queues = {
        tier: Queue()
        for tier in TIER
    }

    cust_stacks: Dict[str, Stack] = {}

    bst_katalog = BSTKatalog()

    graph_rek = GraphRekomendasi()

    completed_orders: List[Order] = []

    order_counter = 0

    order_stack = Stack(kapasitas=10000)

    canceled_orders = set()

    customer_history: Dict[str, List[str]] = {}

    for p in generate_produk(100):
        bst_katalog.insert(p)

    print("=" * 70)
    print("E-Commerce Order Management".center(70))
    print("=" * 70)

    while True:

        cmd = input("> ").strip()

        if not cmd:
            continue

        parts = cmd.split()

        perintah = parts[0].upper()

        # lanjutkan isi CLI dari kode asli lu
        # ORDER
        # SERVE
        # CANCEL_LAST
        # RIWAYAT
        # LAPORAN_HARIAN
        # dll


if __name__ == "__main__":
    main()
