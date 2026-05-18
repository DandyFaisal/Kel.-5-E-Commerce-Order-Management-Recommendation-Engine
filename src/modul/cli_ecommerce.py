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

    last_customer = None

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
                print("\n" + "="*70)
                print("DAFTAR PERINTAH".ljust(70))
                print("="*70)
                print("  ORDER <cust> <prod> <tier>     - Tambah order")
                print("  SERVE                          - Layani order PREMIUM→REGULAR→ECONOMY")
                print("  CANCEL_LAST                    - Batalkan order terakhir")
                print("  CARI_PRODUK <kode>             - Cari produk")
                print("  UPDATE_STOK <kode> <qty>       - Update stok")
                print("  REKOMENDASI <kode_produk>      - Rekomendasi produk")
                print("  RIWAYAT <cust>                 - Riwayat order pelanggan")
                print("  LAPORAN_HARIAN                 - Laporan order")
                print("  KELUAR                         - Keluar program")
                print("="*70 + "\n")

            elif perintah == "ORDER" and len(parts) >= 4:
                pelanggan, produk, tier_str = parts[1], parts[2], parts[3].upper()
                if tier_str not in TIER:
                    print(f"[ERROR] Tier '{tier_str}' tidak valid. Gunakan: PREMIUM, REGULAR, ECONOMY")
                    continue

                produk_obj = bst_katalog.search(produk)
                if not produk_obj:
                    print(f"[ERROR] Produk '{produk}' tidak ditemukan")
                    continue

                if produk_obj.stok <= 0:
                    print(f"[ERROR] Stok produk '{produk}' habis")
                    continue

                order_counter += 1
                order = Order(
                    order_id=order_counter,
                    pelanggan=pelanggan,
                    produk_kode=produk,
                    tier=TIER[tier_str],
                    qty=1,
                    total_harga=produk_obj.harga,
                    waktu_pesan=time.time()
                )

                queues[tier_str].enqueue(order)
                bst_katalog.update_stok(produk, -1)

                if pelanggan not in customer_history:
                    customer_history[pelanggan] = []
                customer_history[pelanggan].append(produk)

                last_customer = pelanggan
                graph_rek.add_copurchase(produk, produk)

                print(f"[OK] Order #{order_counter} dari {pelanggan} - {produk_obj.nama} (Rp{produk_obj.harga:,.0f})")

            elif perintah == "SERVE":
                served = False
                for tier_name in ['PREMIUM', 'REGULAR', 'ECONOMY']:
                    if not queues[tier_name].is_empty():
                        order = queues[tier_name].dequeue()
                        completed_orders.append(order)
                        produk_obj = bst_katalog.search(order.produk_kode)
                        print(f"[SERVED] Order #{order.order_id} ({TIER_NAME[order.tier]}) - {order.pelanggan} | {produk_obj.nama}")
                        served = True
                        break
                if not served:
                    print("[INFO] Tidak ada order yang harus dilayani")

            elif perintah == "CANCEL_LAST":
                if last_customer:
                    for tier_name in ['PREMIUM', 'REGULAR', 'ECONOMY']:
                        found = queues[tier_name].remove_by_condition(
                            lambda o: o.pelanggan == last_customer
                        )
                        if found:
                            canceled_orders.add(last_customer)
                            print(f"[OK] Order terakhir dari {last_customer} dibatalkan")
                            break
                    if not found:
                        print(f"[INFO] Tidak ada order dari {last_customer}")
                else:
                    print("[INFO] Belum ada order sebelumnya")

            elif perintah == "CARI_PRODUK" and len(parts) >= 2:
                kode = parts[1]
                produk_obj = bst_katalog.search(kode)
                if produk_obj:
                    print(f"[FOUND] {produk_obj.kode} - {produk_obj.nama} | Rp{produk_obj.harga:,.0f} | Stok: {produk_obj.stok}")
                else:
                    print(f"[NOT FOUND] Produk '{kode}' tidak ditemukan")

            elif perintah == "UPDATE_STOK" and len(parts) >= 3:
                kode, qty_str = parts[1], parts[2]
                try:
                    qty_delta = int(qty_str)
                    if bst_katalog.update_stok(kode, qty_delta):
                        produk_obj = bst_katalog.search(kode)
                        print(f"[OK] Stok {kode} diperbarui. Stok baru: {produk_obj.stok}")
                    else:
                        print(f"[ERROR] Produk '{kode}' tidak ditemukan")
                except ValueError:
                    print(f"[ERROR] Qty harus angka")

            elif perintah == "REKOMENDASI" and len(parts) >= 2:
                kode = parts[1]
                rekomendasi = graph_rek.rekomendasi(kode)
                if rekomendasi:
                    print(f"[REKOMENDASI] Produk terkait {kode}: {', '.join(rekomendasi)}")
                else:
                    print(f"[INFO] Tidak ada rekomendasi untuk {kode}")

            elif perintah == "RIWAYAT" and len(parts) >= 2:
                pelanggan = parts[1]
                if pelanggan in customer_history:
                    produk_list = customer_history[pelanggan]
                    print(f"[RIWAYAT] {pelanggan}: {', '.join(produk_list)}")
                else:
                    print(f"[INFO] {pelanggan} belum melakukan order")

            elif perintah == "LAPORAN_HARIAN":
                if completed_orders:
                    print("\n[LAPORAN HARIAN]")
                    print(f"Total Order Selesai: {len(completed_orders)}")
                    sorted_by_harga = bubble_sort_by_harga(completed_orders)
                    print("\nTop 5 Order (by Harga):")
                    for order in sorted_by_harga[:5]:
                        produk_obj = bst_katalog.search(order.produk_kode)
                        print(f"  #{order.order_id} - {order.pelanggan} | {produk_obj.nama} | Rp{order.total_harga:,.0f}")
                else:
                    print("[INFO] Belum ada order yang selesai")

            elif perintah == "KELUAR":
                print("Terima kasih telah menggunakan sistem ini!")
                break

            else:
                print(f"[ERROR] Perintah '{perintah}' tidak dikenali. Ketik BANTUAN untuk bantuan.")

        except Exception as e:
            print(f"[ERROR] {str(e)}")


if __name__ == "__main__":
    main()
