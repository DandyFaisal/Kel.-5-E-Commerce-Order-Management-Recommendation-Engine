import random
from dataclasses import dataclass

random.seed(99)

TIER = {'PREMIUM': 1, 'REGULAR': 2, 'ECONOMY': 3}
TIER_NAME = {v: k for k, v in TIER.items()}

@dataclass
class Produk:
    kode: str
    nama: str
    harga: float
    stok: int

@dataclass
class Order:
    order_id: int
    pelanggan: str
    produk_kode: str
    tier: int
    qty: int
    total_harga: float
    waktu_pesan: float
