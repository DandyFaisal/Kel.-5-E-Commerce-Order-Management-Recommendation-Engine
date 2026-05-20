# 🛒 KELOMPOK-5  
# E-Commerce Order Management & Recommendation Engine

> Topik 3 - Algoritma dan Struktur Data

---

# 👥 ANGGOTA KELOMPOK

| No | Nama | NIM |
|---|---|---|
| 1 | Dandy Faisal Bimasena | 25051030062 |
| 2 | Dewangga Dai Prabawa | 25051030058 |
| 3 | Muhammad Fathir Al Malik | 25051030067 |
| 4 | Muhammad Raykhan Faddillah | 25051030057 |

---

# 📚 MATA KULIAH

- **Algoritma dan Struktur Data**
- S1 Teknik Elektro
- Universitas Negeri Yogyakarta

---

# 📖 DESKRIPSI PROYEK

Proyek ini merupakan simulasi sistem manajemen pesanan (**Order Management System**) pada platform **E-Commerce** menggunakan bahasa pemrograman Python.

Program mengimplementasikan berbagai struktur data dan algoritma dalam satu sistem terintegrasi, seperti:

- Queue
- Stack
- Binary Search Tree (BST)
- Graph
- Sorting Algorithm
- Benchmark Runtime

Program berjalan menggunakan **Command Line Interface (CLI)** sehingga pengguna dapat melakukan simulasi transaksi secara langsung.

---

# 🎯 TUJUAN PROYEK

Tujuan dari proyek ini adalah:

- Mengimplementasikan struktur data pada kasus nyata
- Memahami kompleksitas algoritma
- Melakukan analisis performa program
- Membuat sistem E-Commerce sederhana berbasis CLI
- Mengintegrasikan beberapa struktur data dalam satu program

---

# 🧩 STRUKTUR DATA YANG DIGUNAKAN

## 1️⃣ Linked List

Digunakan sebagai dasar pembuatan node melalui class `LLNode`.

### Fungsi:
- Menjadi fondasi Queue
- Menjadi fondasi Stack

---

## 2️⃣ Queue (FIFO)

Diimplementasikan pada class `Queue`.

### Prinsip:
> First In First Out (FIFO)

### Fungsi:
- Menyimpan antrian order pelanggan
- Prioritas berdasarkan tier:
  - PREMIUM
  - REGULAR
  - ECONOMY

### Kompleksitas:
| Operasi | Kompleksitas |
|---|---|
| Enqueue | O(1) |
| Dequeue | O(1) |

---

## 3️⃣ Stack (LIFO)

Diimplementasikan pada class `Stack`.

### Prinsip:
> Last In First Out (LIFO)

### Fungsi:
- Menyimpan riwayat transaksi
- Undo / Cancel order terakhir

### Kompleksitas:
| Operasi | Kompleksitas |
|---|---|
| Push | O(1) |
| Pop | O(1) |

---

## 4️⃣ Binary Search Tree (BST)

Diimplementasikan pada:
- `BSTNode`
- `BSTKatalog`

### Fungsi:
- Menyimpan katalog produk
- Pencarian produk
- Update stok
- Traversal data produk

### Kompleksitas:
| Operasi | Kompleksitas |
|---|---|
| Insert | O(log n) |
| Search | O(log n) |
| Update | O(log n) |

---

## 5️⃣ Graph

Diimplementasikan pada class `GraphRekomendasi`.

### Fungsi:
- Menyimpan hubungan antar produk
- Sistem rekomendasi produk

### Algoritma:
- Breadth First Search (BFS)

### Kompleksitas:
```math
O(V + E)
```

---

## 6️⃣ Dictionary (Hash Table)

Digunakan untuk:
- Tier pelanggan
- Queue pelanggan
- Relasi graph
- Data pelanggan

### Kelebihan:
- Akses data sangat cepat

---

## 7️⃣ List (Dynamic Array)

Digunakan untuk:
- Menyimpan data produk
- Menyimpan laporan transaksi
- Menyimpan hasil traversal

---

# ⚙️ FITUR PROGRAM

| Fitur | Deskripsi |
|---|---|
| ORDER | Menambahkan order pelanggan |
| SERVE | Memproses order berdasarkan tier |
| CANCEL_LAST | Membatalkan order terakhir |
| CARI_PRODUK | Mencari produk |
| UPDATE_STOK | Mengupdate stok |
| REKOMENDASI | Memberikan rekomendasi produk |
| RIWAYAT | Menampilkan riwayat transaksi |
| LAPORAN_HARIAN | Menampilkan laporan transaksi |
| BANTUAN | Menampilkan daftar command |
| KELUAR | Menutup program |

---

# 🔄 ALGORITMA SORTING

## 🔹 Bubble Sort

Digunakan untuk:
- Sorting berdasarkan total harga

### Kompleksitas:
```math
O(n^2)
```

---

## 🔹 Insertion Sort

Digunakan untuk:
- Sorting berdasarkan waktu transaksi

### Kompleksitas:
```math
O(n^2)
```

---

# 🛠️ ALUR SISTEM

```text
Pelanggan Order
       ↓
Queue berdasarkan Tier
       ↓
SERVE Order
       ↓
BST Update Stok
       ↓
Stack Simpan Riwayat
       ↓
Graph Update Relasi Produk
       ↓
Sistem Rekomendasi BFS
```

---

# 💻 CONTOH PENGGUNAAN PROGRAM

## 📌 Skenario Uji Realistis

```bash
> ORDER C001 P001 PREMIUM
> ORDER C002 P002 REGULAR
> ORDER C003 P003 ECONOMY

> SERVE
Queue akan memproses PREMIUM lebih dulu

> CARI_PRODUK P001
BST melakukan pencarian produk

> UPDATE_STOK P001 10
BST update stok produk

> REKOMENDASI P001
Graph BFS memberikan rekomendasi produk

> RIWAYAT C001
Stack menampilkan riwayat transaksi

> LAPORAN_HARIAN
Bubble Sort & Insertion Sort dijalankan

> CANCEL_LAST
Stack undo order terakhir

> KELUAR
```

---

# 📊 EKSPERIMEN PERFORMA PROGRAM

Program dilengkapi benchmark performa untuk menguji efisiensi algoritma dan struktur data.

---

# 📦 DATASET PENGUJIAN

| Dataset | Jumlah Data |
|---|---|
| Kecil | 50 |
| Sedang | 100 |
| Besar | 300 |

---

# 🧪 MODUL YANG DIUJI

| Modul | Pengujian |
|---|---|
| Bubble Sort | Sorting harga |
| Insertion Sort | Sorting waktu |
| BST Search | Pencarian produk |
| Queue | Proses dequeue |
| Graph BFS | Sistem rekomendasi |

---

# 📈 ANALISIS PERFORMA

## 🔹 Bubble Sort & Insertion Sort

Kompleksitas:

```math
O(n^2)
```

### Hasil:
- Runtime meningkat signifikan saat dataset besar
- Sorting menjadi modul paling berat

---

## 🔹 BST Search

Kompleksitas:

```math
O(log n)
```

### Hasil:
- Pencarian tetap cepat
- Sangat efisien untuk katalog produk

---

## 🔹 Queue

Kompleksitas:

```math
O(1)
```

### Hasil:
- Sangat optimal untuk sistem antrian

---

## 🔹 Graph BFS

Kompleksitas:

```math
O(V + E)
```

### Hasil:
- Efektif untuk rekomendasi produk

---

# 📌 KESIMPULAN EKSPERIMEN

Berdasarkan benchmark:

- Runtime meningkat seiring ukuran dataset
- Sorting memiliki beban terbesar
- BST sangat cepat untuk pencarian
- Queue sangat efisien
- BFS cocok untuk sistem rekomendasi

---

# ✅ KELEBIHAN PROGRAM

- Menggabungkan banyak struktur data
- Simulasi E-Commerce realistis
- Memiliki benchmark performa
- Sistem rekomendasi produk
- Mendukung prioritas pelanggan
- CLI interaktif

---

# ❌ KEKURANGAN PROGRAM

- Belum menggunakan database
- Belum memiliki GUI
- BST belum self-balancing
- Sorting masih O(n²)
- Data masih bersifat sementara

---

# 🚀 PENGEMBANGAN SELANJUTNYA

Pengembangan yang dapat dilakukan:

- Menggunakan AVL Tree
- Menggunakan Merge Sort / Quick Sort
- Menambahkan database SQLite/MySQL
- Membuat GUI berbasis web
- Sistem login pengguna
- Sistem pembayaran

---

# ▶️ CARA MENJALANKAN PROGRAM

## 1️⃣ Clone Repository

```bash
git clone <link-repository>
```

---

## 2️⃣ Masuk ke Folder

```bash
cd nama-folder
```

---

## 3️⃣ Jalankan Program

```bash
python main.py
```

---

# 📂 STRUKTUR FILE

```text
📁 project-folder
│
├── main.py
├── benchmark.py
├── README.md
└── requirements.txt
```

---

# 📌 OUTPUT PROGRAM

Program akan menampilkan:

- Sistem CLI interaktif
- Benchmark performa
- Sorting laporan transaksi
- Sistem rekomendasi produk
- Riwayat transaksi pelanggan

---

# 🏁 PENUTUP

Proyek ini dibuat sebagai implementasi nyata dari materi:

- Struktur Data
- Algoritma
- Analisis Kompleksitas
- Implementasi Sistem Python

Melalui proyek ini diharapkan mahasiswa dapat memahami penerapan struktur data secara langsung dalam pengembangan sistem nyata.

---

# 🙏 TERIMA KASIH

### Kelompok 5  
Algoritma dan Struktur Data  
Universitas Negeri Yogyakarta
