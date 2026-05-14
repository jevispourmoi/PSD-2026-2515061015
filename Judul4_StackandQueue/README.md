**A. Judul Program:** Antrean pesanan robot restoran


**B. Deskripsi Singkat:** 
Program ini adalah simulasi antrean pesanan makanan yang diantar oleh robot menggunakan struktur data Queue Circular Array. Sistem bekerja dengan aturan FIFO 
(First In First Out), yaitu pesanan yang masuk lebih dulu akan diantar lebih dulu. Program memiliki fitur untuk menambahkan pesanan baru (enqueue), 
mengantar pesanan (dequeue), melihat pesanan paling depan (peek), dan menampilkan seluruh antrean (display). Antrean dibuat melingkar (circular queue) 
sehingga index dapat kembali ke awal array saat sudah mencapai batas akhir, sehingga penggunaan array menjadi lebih efisien. Selain itu, program juga menyediakan 
menu interaktif agar pengguna bisa mengatur antrean pesanan robot dengan lebih mudah melalui terminal.

**C. Source Code:**

<img width="1348" height="627" alt="Screenshot 2026-05-14 092038" src="https://github.com/user-attachments/assets/a49ffddf-db22-4385-be00-55775f3110b4" />

Class RobotOrderQueue digunakan untuk membuat sistem antrean pesanan robot dengan konsep circular queue. Pada baris class RobotOrderQueue: program membuat sebuah class 
sebagai wadah seluruh operasi antrean. Lalu pada function __init__(self, max_size=5) program menjalankan proses awal saat objek dibuat. Baris self.MAXN = max_size 
menyimpan kapasitas maksimal antrean, kemudian self.q = [None] * self.MAXN membuat list kosong sesuai ukuran antrean. Setelah itu self.front_idx = -1 dan self.rear_idx = -1
menandakan antrean masih kosong. Function is_empty() digunakan untuk mengecek apakah antrean kosong dengan return self.front_idx == -1. Sedangkan is_full() digunakan untuk 
mengecek apakah antrean penuh menggunakan (self.rear_idx + 1) % self.MAXN == self.front_idx, karena queue dibuat melingkar sehingga index bisa kembali ke awal. Pada function 
enqueue(self, detail_pesanan), program menambahkan data baru ke antrean. Pertama program mengecek apakah antrean penuh dengan if self.is_full(). Jika penuh, program menampilkan 
pesan lalu return untuk menghentikan proses. Jika antrean kosong, maka front_idx dan rear_idx diatur menjadi 0 karena data pertama masuk di index awal. Jika tidak kosong, 
maka rear_idx maju satu langkah menggunakan (self.rear_idx + 1) % self.MAXN. Setelah itu data disimpan ke dalam queue menggunakan self.q[self.rear_idx] = detail_pesanan, 
lalu program menampilkan pesan bahwa pesanan berhasil masuk antrean.

<img width="1212" height="796" alt="Screenshot 2026-05-14 092050" src="https://github.com/user-attachments/assets/5e4ffd4d-0513-45d4-b0eb-bdcee37fe29b" />

Pada function dequeue(), program digunakan untuk menghapus atau memproses pesanan paling depan. Program pertama mengecek apakah antrean kosong 
menggunakan if self.is_empty(). Jika kosong, program menampilkan pesan lalu berhenti dengan return. Jika tidak kosong, program menampilkan pesanan 
yang sedang diantar robot menggunakan self.q[self.front_idx], kemudian menampilkan simulasi perjalanan robot. Setelah itu program mengecek apakah 
antrean hanya memiliki satu data dengan if self.front_idx == self.rear_idx. Jika iya, maka front_idx dan rear_idx dikembalikan menjadi -1 karena 
antrean menjadi kosong. Jika masih ada data lain, maka front_idx dipindahkan ke index berikutnya menggunakan (self.front_idx + 1) % self.MAXN. 
Function peek() digunakan untuk melihat pesanan paling depan tanpa menghapusnya. Program mengecek antrean kosong atau tidak, lalu menampilkan data 
pada posisi front_idx. Sedangkan function display() digunakan untuk menampilkan seluruh antrean. Program pertama mengecek apakah antrean kosong. 
Jika tidak kosong, program membuat variabel i = self.front_idx untuk memulai penelusuran dari data paling depan. Kemudian while True digunakan untuk 
melakukan perulangan terus-menerus. Data pada index i ditampilkan menggunakan print(self.q[i]). Setelah itu program mengecek apakah i sudah mencapai rear_idx. 
Jika sudah, loop dihentikan menggunakan break. Jika belum, maka i dipindahkan ke index berikutnya menggunakan (i + 1) % self.MAXN agar queue bisa berjalan 
melingkar dan kembali ke index awal jika sudah mencapai index terakhir.

<img width="1256" height="834" alt="Screenshot 2026-05-14 092059" src="https://github.com/user-attachments/assets/23131c85-e251-4c2c-bd96-e04a307c984a" />
<img width="934" height="64" alt="Screenshot 2026-05-14 092554" src="https://github.com/user-attachments/assets/10c66c9a-ab47-430c-9754-3d7561d08388" />

Pada function main(), program menjalankan seluruh menu utama sistem antrean robot. Baris robot = RobotOrderQueue(5) membuat objek antrean dengan 
kapasitas maksimal lima pesanan. Variabel pilih = 0 digunakan untuk menyimpan pilihan menu dari user. Kemudian while pilih != 5 membuat program terus 
berjalan sampai user memilih keluar. Program menampilkan daftar menu menggunakan beberapa print(), seperti menambah pesanan, mengantar pesanan, 
melihat pesanan terdepan, dan menampilkan seluruh antrean. Pada bagian try, program mencoba membaca input angka dari user menggunakan pilih = int(input("Pilih: ")). 
Jika user memasukkan selain angka, maka except ValueError akan menampilkan pesan error dan continue digunakan untuk kembali ke menu awal. Jika user memilih menu 1, 
program meminta input nama menu dan nomor meja, lalu menggabungkannya menjadi satu string menggunakan f"{nama_menu} ke Meja {no_meja}", kemudian data dimasukkan 
ke antrean dengan robot.enqueue(data_lengkap). Jika memilih 2, program menjalankan robot.dequeue(). Jika memilih 3, program menjalankan robot.peek(). Jika memilih 4, 
program menjalankan robot.display(). Jika memilih 5, program menampilkan pesan bahwa sistem dimatikan. Selain itu, jika input tidak sesuai pilihan menu, 
program menampilkan pesan “Pilihan tidak valid!”. Terakhir, pada bagian if __name__ == "__main__":, Python mengecek apakah file dijalankan langsung, lalu main() 
dipanggil untuk menjalankan seluruh program.

**D. Output:**

<img width="1528" height="672" alt="Screenshot 2026-05-14 094554" src="https://github.com/user-attachments/assets/2230c5b1-5c6d-4df9-9615-d1d76ded4c86" />

Di potongan gambar output kode yang ini menunjukkan bahwa chef atau pengguna memilih opsi 1, yaitu input nama menu pesanan dan juga nomor meja. Dilihat dari gambar, 
pengguna menginputkan dua data baru.

<img width="1328" height="324" alt="Screenshot 2026-05-14 094610" src="https://github.com/user-attachments/assets/1b4cd9da-51a9-4c71-a62d-bbcc8de5c037" />

Lalu pada gambar yang kedua ini, pengguna menginputkan data ketiga.

<img width="1170" height="713" alt="Screenshot 2026-05-14 094624" src="https://github.com/user-attachments/assets/c9505bb7-dde1-4cd0-934b-5a56ac6d8750" />

Pada gambar ke-3 ini, pengguna memilih opsi 2, yaitu dequeue data atau diprogram ini robot akan mengantarkan pesanan ke meja pelanggan yang sudah diinputkan. 
Lalu, pengguna juga memilih opsi 3 untuk mengecek pesanan selanjutnya yang harus diantarkan, lalu memilih opsi 2 lagi untuk mengantarkan pesanan tersebut.

<img width="1063" height="498" alt="Screenshot 2026-05-14 094634" src="https://github.com/user-attachments/assets/17f8ffe3-1cab-45f4-8911-7d0be1238944" />

Dan pada gambar terakhir ini, pengguna memilih opsi 4 untuk melihat seluruh daftar antrean yang tersisa. Setelah itu, pengguna memilih opsi 5 untuk keluar dari proggram.

**E. Link Youtube**
https://youtu.be/0oQSIgnCSKw
