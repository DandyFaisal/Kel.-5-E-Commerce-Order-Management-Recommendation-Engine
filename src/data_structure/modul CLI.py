import numpy as np, time, random
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple

# Import dari modul yang sudah dipisah
from models import Produk, Order
from queue import Queue, LLNode as QueueLLNode  # LLNode dari queue
from stack import Stack, LLNode as StackLLNode
from bst import BSTKatalog, BSTNode
from graph import GraphRekomendasi
from sort_utils import OrderNode, bubble_sort_by_total_harga_desc, insertion_sort_by_waktu_pesan_asc

np.random.seed(99)
random.seed(99)

TIER = {'PREMIUM': 1, 'REGULAR': 2, 'ECONOMY': 3}

# Generator data awal (tidak berubah)
def generate_produk(n=100) -> List[Produk]:
    nama_template = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset',
                     'Webcam', 'USB Hub', 'Charger', 'Kabel HDMI', 'Speaker']

    produk_list = []
    for i in range(1, n + 1):
        kode = f'P{i:03d}'
        nama = f"{random.choice(nama_template)} Model-{i}"
        harga = round(random.uniform(50_000, 5_000_000), -3)
        stok = random.randint(0, 200)
        produk_list.append(Produk(kode, nama, harga, stok))
    return produk_list

def main():
    # Inisialisasi
    queues = {tier: Queue() for tier in TIER}
    cust_stacks: Dict[str, Stack] = {}
    bst_katalog = BSTKatalog()
    graph_rek = GraphRekomendasi()
    order_counter = 0

    for p in generate_produk(100):
        bst_katalog.insert(p)

    print("E-Commerce Order Management  Ketik BANTUAN untuk daftar perintah")
    # TODO: implementasikan loop CLI

if __name__ == "__main__":
    main()
