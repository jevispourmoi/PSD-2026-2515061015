class Node:
    def __init__(self, skor, nama):
        self.skor = skor   
        self.nama = nama
        self.left = None
        self.right = None


class ArcadeBST:
    def __init__(self):
        self.root = None

    def insert(self, root, skor, nama):
        if root is None:
            return Node(skor, nama)
        if skor < root.skor:
            root.left = self.insert(root.left, skor, nama)
        elif skor > root.skor:
            root.right = self.insert(root.right, skor, nama)
        else:
            print(f"Skor {skor} sudah ada!")
        return root

    def tambah_skor(self, skor, nama):
        self.root = self.insert(self.root, skor, nama)
        print(f"Skor {skor} atas nama {nama} berhasil ditambahkan.")

    def search(self, root, skor):
        if root is None:
            return None
        if root.skor == skor:
            return root
        if skor < root.skor:
            return self.search(root.left, skor)
        return self.search(root.right, skor)

    def cari_skor(self, skor):
        node = self.search(self.root, skor)
        if node:
            print(f"Ditemukan: {node.nama} dengan skor {node.skor}")
        else:
            print(f"Skor {skor} tidak ditemukan.")

    def find_min_node(self, root):
        while root.left is not None:
            root = root.left
        return root

    def delete(self, root, skor):
        if root is None:
            return None
        if skor < root.skor:
            root.left = self.delete(root.left, skor)
        elif skor > root.skor:
            root.right = self.delete(root.right, skor)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.find_min_node(root.right)
            root.skor = successor.skor
            root.nama = successor.nama
            root.right = self.delete(root.right, successor.skor)
        return root

    def hapus_skor(self, skor):
        if self.search(self.root, skor):
            self.root = self.delete(self.root, skor)
            print(f"Skor {skor} berhasil dihapus.")
        else:
            print(f"Skor {skor} tidak ditemukan.")

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"  {root.skor:>8} - {root.nama}")
        self.inorder(root.right)

    def tampilkan_papan_skor(self):
        if self.root is None:
            print("Belum ada skor.")
            return
        print(f"{'Skor':>8}   Nama")
        print("  " + "-" * 25)
        self.inorder(self.root)

    def skor_terendah(self):
        if self.root is None:
            print("Belum ada skor.")
            return
        node = self.find_min_node(self.root)
        print(f"Skor terendah: {node.skor} ({node.nama})")

    def skor_tertinggi(self):
        if self.root is None:
            print("Belum ada skor.")
            return
        current = self.root
        while current.right is not None:
            current = current.right
        print(f"Skor tertinggi: {current.skor} ({current.nama})")

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def total_pemain(self):
        print(f"Total pemain: {self.count_nodes(self.root)}")

    def find_successor(self, root, skor):
        current = root
        successor = None
        found = False
        while current:
            if skor < current.skor:
                successor = current
                current = current.left
            elif skor > current.skor:
                current = current.right
            else:
                found = True
                if current.right:
                    successor = self.find_min_node(current.right)
                break
        return successor, found

    def skor_diatas(self, skor):
        node, found = self.find_successor(self.root, skor)
        if not found:
            print(f"Skor {skor} tidak ditemukan.")
        elif node:
            print(f"Skor tepat di atas {skor}: {node.skor} ({node.nama})")
        else:
            print(f"{skor} adalah skor tertinggi, tidak ada di atasnya.")


def main():
    bst = ArcadeBST()
    pilih = 0

    while pilih != 9:
        print("\n=== PAPAN SKOR GAME ARCADE ===")
        print("1. Tambah skor")
        print("2. Cari skor")
        print("3. Hapus skor")
        print("4. Tampilkan papan skor")
        print("5. Skor terendah")
        print("6. Skor tertinggi")
        print("7. Total pemain")
        print("8. Skor tepat di atas nilai tertentu (successor)")
        print("9. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                skor = int(input("Masukkan skor: "))
                nama = input("Nama pemain: ").strip()
                bst.tambah_skor(skor, nama)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                skor = int(input("Cari skor: "))
                bst.cari_skor(skor)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                skor = int(input("Hapus skor: "))
                bst.hapus_skor(skor)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            bst.tampilkan_papan_skor()

        elif pilih == 5:
            bst.skor_terendah()

        elif pilih == 6:
            bst.skor_tertinggi()

        elif pilih == 7:
            bst.total_pemain()

        elif pilih == 8:
            try:
                skor = int(input("Masukkan skor acuan: "))
                bst.skor_diatas(skor)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 9:
            print("Game over!")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()