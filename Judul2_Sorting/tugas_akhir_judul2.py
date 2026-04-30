def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j]["harga"] < arr[pos]["harga"]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)


def main():
    try:
        n = int(input("Masukkan jumlah produk: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data produk:")
    for i in range(n):
        nama = input(f"Nama produk ke-{i+1}: ")
        while True:
            try:
                harga = int(input(f"Harga produk ke-{i+1}: "))
                break
            except ValueError:
                print("Input tidak valid, masukkan angka!")
        arr.append({"nama": nama, "harga": harga})

    print("\nProduk sebelum diurutkan:")
    for p in arr:
        print(f"{p['nama']} - Rp {p['harga']}")

    selection_sort(arr, n)

    print("\nProduk setelah diurutkan:")
    for p in arr:
        print(f"{p['nama']} - Rp {p['harga']}")


if __name__ == "__main__":
    main()