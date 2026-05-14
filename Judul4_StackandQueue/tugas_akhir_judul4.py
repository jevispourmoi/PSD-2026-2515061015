class RobotOrderQueue:
    def __init__(self, max_size=5):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, detail_pesanan):
        if self.is_full():
            print("\nAntrean Penuh, tunggu pesanan lain selesai.")
            return
        
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
            
        self.q[self.rear_idx] = detail_pesanan
        print(f"\nBerhasil: '{detail_pesanan}' masuk ke jadwal antar robot.")

    def dequeue(self):
        if self.is_empty():
            print("\nTidak ada pesanan di antrean.")
            return
        
        print(f"\nRobot bergerak mengantar: {self.q[self.front_idx]}")
        print("... Robot sedang dalam perjalanan...")
        print("... Pesanan telah sampai. Robot kembali ke dapur.")
        
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("\nTidak ada pesanan di antrean.")
            return
        print(f"\nPesanan berikutnya yang harus diantar: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("\nTidak ada antrean pesanan.")
            return
        print("\n=== DAFTAR ANTRIAN TUGAS ROBOT ===")
        i = self.front_idx
        while True:
            print(f" > {self.q[i]}")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print("==================================")


def main():
    robot = RobotOrderQueue(5)
    pilih = 0
    
    while pilih != 5:
        print("\n--- MENU KONTROL ROBOT ---")
        print("1. Tambah Pesanan Baru (Input Chef)")
        print("2. Kirim Robot (Antar Pesanan)")
        print("3. Cek Pesanan Terdepan")
        print("4. Tampilkan Seluruh Antrean")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Peringatan: Masukkan angka 1-5!")
            continue
            
        if pilih == 1:
            print("\n--- Input Pesanan Baru ---")
            nama_menu = input("Nama Menu   : ")
            no_meja = input("Nomor Meja  : ")
            data_lengkap = f"{nama_menu} ke Meja {no_meja}"
            robot.enqueue(data_lengkap)
        elif pilih == 2:
            robot.dequeue()
        elif pilih == 3:
            robot.peek()
        elif pilih == 4:
            robot.display()
        elif pilih == 5:
            print("Sistem dimatikan.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()