from main import BSTKatalog, Produk

def test_insert_produk():
    bst = BSTKatalog()

    produk = Produk(
        "P001",
        "Laptop Gaming",
        10000000,
        5
    )

    bst.insert(produk)

    hasil = bst.search("P001")

    assert hasil is not None

def test_search_produk():
    bst = BSTKatalog()

    produk = Produk(
        "P002",
        "Mouse",
        150000,
        10
    )

    bst.insert(produk)

    hasil = bst.search("P002")

    assert hasil.nama == "Mouse"

def test_update_stok():
    bst = BSTKatalog()

    produk = Produk(
        "P003",
        "Keyboard",
        300000,
        5
    )

    bst.insert(produk)

    bst.update_stok("P003", 10)

    hasil = bst.search("P003")

    assert hasil.stok == 15