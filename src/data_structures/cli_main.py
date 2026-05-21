import time
import random
from typing import Dict, List

from models import Produk, Order, TIER
from queue import Queue, LLNode as QueueLLNode
from stack import Stack, LLNode as StackLLNode
from bst import BSTKatalog, BSTNode

random.seed(99)


def generate_produk(n=100) -> List[Produk]:
    """Generate produk dummy untuk testing."""
    nama_template = [
        'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset',
        'Webcam', 'USB Hub', 'Charger', 'Kabel HDMI', 'Speaker'
    ]

    produk_list = []
    for i in range(1, n + 1):
        kode = f'P{i:03d}'
        nama = f"{random.choice(nama_template)} Model-{i}"
        harga = round(random.uniform(50_000, 5_000_000), -3)
        stok = random.randint(0, 200)
        produk_list.append(Produk(kode, nama, harga, stok))

    return produk_list


def main():
    """Main CLI application."""
    # Initialize data structures
    queues = {tier: Queue() for tier in TIER}
    cust_stacks: Dict[str, Stack] = {}
    bst_katalog = BSTKatalog()
    completed_orders: List[Order] = []
    order_counter = 0
    order_stack = Stack(kapasitas=10000)
    canceled_orders = set()
    customer_history: Dict[str, List[str]] = {}

    # Load catalog
    for p in generate_produk(100):
        bst_katalog.insert(p)

    print("=" * 70)
    print("E-Commerce Order Management & Recommendation Engine".center(70))
    print("=" * 70)
    print("Ketik BANTUAN untuk daftar perintah\n")

    while True:
        try:
            cmd = input("> ").strip()

            if not cmd:
                continue

            parts = cmd.split()
            perintah = parts[0].upper()

            if perintah == "BANTUAN":
                print("\n" + "=" * 70)
                print("DAFTAR PERINTAH".ljust(70))
                print("=" * 70)
                print("  ORDER <cust> <prod> <tier>     - Tambah order")
                print("  SERVE                          - Layani order")
                print("  CARI_PRODUK <kode>             - Cari produk")
                print("  LIHAT_KATALOG                  - Lihat semua produk")
                print("  KELUAR                         - Keluar program")
                print("=" * 70 + "\n")

            elif perintah == "ORDER" and len(parts) >= 4:
                pelanggan, produk, tier_str = parts[1], parts[2], parts[3].upper()
                if tier_str in TIER:
                    print(f"✓ Order ditambahkan: {pelanggan} -> {produk} ({tier_str})")
                else:
                    print(f"✗ Tier tidak valid: {tier_str}")

            elif perintah == "CARI_PRODUK" and len(parts) >= 2:
                kode = parts[1]
                produk = bst_katalog.search(kode)
                if produk:
                    print(f"✓ Produk ditemukan: {produk.kode} - {produk.nama} "
                          f"(Harga: {produk.harga}, Stok: {produk.stok})")
                else:
                    print(f"✗ Produk tidak ditemukan: {kode}")

            elif perintah == "LIHAT_KATALOG":
                produk_list = bst_katalog.inorder()
                print(f"\n{'Kode':<8} {'Nama':<30} {'Harga':<15} {'Stok':<8}")
                print("-" * 70)
                for p in produk_list[:10]:  # Show first 10
                    print(f"{p.kode:<8} {p.nama:<30} {p.harga:<15.0f} {p.stok:<8}")
                if len(produk_list) > 10:
                    print(f"... dan {len(produk_list) - 10} produk lainnya")

            elif perintah == "KELUAR":
                print("Terima kasih! Sampai jumpa.")
                break

            else:
                print("✗ Perintah tidak dikenali. Ketik BANTUAN untuk bantuan.")

        except KeyboardInterrupt:
            print("\n\nProgram dihentikan.")
            break
        except Exception as e:
            print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
