def sequential_search(data_buku, n, target):
    i = 0
    pos = -1
    while i < n:
        if data_buku[i] == target:
            pos = i
            break
        i += 1
    return pos


def main():
    data_buku = [
        "Jaringan Komputer",
        "Struktur Data",
        "Matematika Diskrit",
        "Algoritma Pemrograman",
        "Cybersecurity",
        "Teknik Digital",
        "Dasar Pemrograman Python",
        "Logika Komputer",
        "Kalkulus",
        "Etika Profesi IT",
    ]

    rak = ["Rak D4", "Rak A3", "Rak C3", "Rak A1", "Rak D2", "Rak C1", "Rak B2", "Rak D1", "Rak B1","Rak B4",]

    n = len(data_buku)

    print("Daftar Judul Buku")
    for i, target in enumerate(data_buku):
        print(f"{i}. {target}")

    while True:
        target = input("\nMasukkan judul buku yang ingin dicari (atau 'keluar'): ")

        if target.lower() == "keluar":
            break

        pos = sequential_search(data_buku, n, target)

        if pos != -1:
            print(f"Buku {target} ditemukan di {rak[pos]}")
        else:
            print(f"Buku {target} tidak ditemukan.")


if __name__ == "__main__":
    main()

