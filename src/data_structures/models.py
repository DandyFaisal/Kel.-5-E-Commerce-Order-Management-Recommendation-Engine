import time

class Produk:
    def __init__(self, kode: str, nama: str, harga: float, stok: int):
        self.kode = kode                 # P001-P100
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Order:
    def __init__(self, order_id: int, pelanggan: str, produk_kode: str, tier: int, qty: int, total_harga: float, waktu_pesan: float):
        self.order_id = order_id
        self.pelanggan = pelanggan            # C001-C050
        self.produk_kode = produk_kode
        self.tier = tier                 # 1=PREMIUM, 2=REGULAR, 3=ECONOMY
        self.qty = qty
        self.total_harga = total_harga
        self.waktu_pesan = waktu_pesan        # time.time()
