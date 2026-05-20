from typing import Optional, List
from models import Produk


class BSTNode:
    def __init__(self, produk: Produk):
        self.produk = produk
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


class BSTKatalog:
    """Binary Search Tree untuk katalog produk."""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, produk: Produk) -> None:
        """Sisipkan produk berdasarkan kode (string comparison)."""
        if self.root is None:
            self.root = BSTNode(produk)
        else:
            self._insert_recursive(self.root, produk)

    def _insert_recursive(self, node: BSTNode, produk: Produk) -> None:
        """Helper recursive untuk insert."""
        if produk.kode < node.produk.kode:
            if node.left is None:
                node.left = BSTNode(produk)
            else:
                self._insert_recursive(node.left, produk)
        else:
            if node.right is None:
                node.right = BSTNode(produk)
            else:
                self._insert_recursive(node.right, produk)

    def search(self, kode: str) -> Optional[Produk]:
        """Cari produk berdasarkan kode."""
        return self._search_recursive(self.root, kode)

    def _search_recursive(self, node: Optional[BSTNode], kode: str) -> Optional[Produk]:
        """Helper recursive untuk search."""
        if node is None:
            return None
        if kode == node.produk.kode:
            return node.produk
        elif kode < node.produk.kode:
            return self._search_recursive(node.left, kode)
        else:
            return self._search_recursive(node.right, kode)

    def update_stok(self, kode: str, qty_delta: int) -> bool:
        """Update stok produk. Return True jika berhasil."""
        produk = self.search(kode)
        if produk is None:
            return False
        produk.stok += qty_delta
        return True

    def inorder(self) -> List[Produk]:
        """Kembalikan list Produk terurut berdasarkan kode."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[BSTNode], result: List[Produk]) -> None:
        """Helper recursive untuk inorder traversal."""
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.produk)
        self._inorder_recursive(node.right, result)
