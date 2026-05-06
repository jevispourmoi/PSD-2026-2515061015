def sequential_search(data, n, target):
    i = 0
    pos = -1
    while i < n:
        if data[i] == target:
            pos = i
            break
        i += 1
    return pos


def main():
    data = [
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

    n = len(data)

    print("Daftar Judul Buku")
    for i, judul in enumerate(data):
        print(f"{i}. {judul}")

    while True:
        judul_buku = input("\nMasukkan judul buku yang ingin dicari (atau 'keluar'): ")

        if judul_buku.lower() == "keluar":
            break

        pos = sequential_search(data, n, judul_buku)

        if pos != -1:
            print(f"Buku {judul_buku} ditemukan di {rak[pos]}")
        else:
            print(f"Buku {judul_buku} tidak ditemukan.")


if __name__ == "__main__":
    main()