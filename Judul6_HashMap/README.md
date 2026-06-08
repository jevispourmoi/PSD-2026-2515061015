**A. Judul Program:** Proses Login Game RPG dengan Struktur Data Hash Map

**B. Deskripsi Singkat:** 
Program ini mensimulasikan sistem login akun game RPG menggunakan struktur data HashMap dengan metode Open Addressing (Linear Probing). 
Data akun berupa Player ID dan Username disimpan ke dalam tabel hash, kemudian dicari kembali saat proses login.

**C. Source Code:**
<img width="839" height="243" alt="Screenshot 2026-06-08 205250" src="https://github.com/user-attachments/assets/deb03744-295a-422b-8549-e74966a42ec4" />

Pada baris 1, program mendefinisikan sebuah kelas bernama SlotState. Kelas ini berfungsi sebagai tempat untuk menyimpan daftar status
atau kondisi dari sebuah slot penyimpanan. Di baris 2, program membuat penanda EMPTY yang diberi nilai angka 0, yang digunakan untuk 
menunjukkan bahwa sebuah slot dalam keadaan kosong. Pada baris 3, program membuat penanda OCCUPIED yang diberi nilai angka 1, yang 
digunakan untuk menunjukkan bahwa slot tersebut sedang terisi oleh data. Pada baris 6, program mendefinisikan kelas bernama AkunPlayer 
yang digunakan sebagai kerangka untuk menyimpan informasi akun pemain. Baris 7 memuat fungsi __init__ yang akan langsung bekerja untuk
menyiapkan data awal setiap kali ada objek akun baru yang dibuat. Di baris 8 dan 9, program menyiapkan variabel self.player_id dan 
self.username yang keduanya diberikan nilai awal None, yang berarti nomor identitas dan nama pengguna untuk akun tersebut masih kosong 
atau belum diisi. Terakhir pada baris 10, program mengatur variabel self.state dengan memberikan nilai awal SlotState.EMPTY 
(mengambil status dari kelas di atasnya), yang menegaskan bahwa posisi data akun ini pada awalnya berstatus kosong dan siap untuk diisi.


<img width="1319" height="633" alt="Screenshot 2026-06-08 205258" src="https://github.com/user-attachments/assets/413e764f-0f62-4964-a79e-f5fcc0ae2ed9" />

Pada baris 13, program mendefinisikan sebuah kelas bernama HashMapAkunGame yang berfungsi sebagai struktur data utama penyimpan akun. 
Baris 14 memuat fungsi __init__ yang akan berjalan pertama kali ketika struktur ini dibentuk, dengan parameter size=10 yang mengatur 
ukuran kapasitas bawaannya adalah 10 posisi. Pada baris 15, nilai kapasitas tersebut disimpan secara permanen ke dalam variabel self.SIZE. 
Selanjutnya di baris 16, program membuat daftar panjang bernama self.table. Daftar ini diisi dengan kumpulan objek kosong dari cetakan 
AkunPlayer secara berulang, sebanyak angka yang ada di dalam variabel self.SIZE. Baris 18 mendefinisikan fungsi hash_function yang memiliki 
tugas khusus untuk menghitung dan menentukan di posisi indeks mana sebuah data player_id harus diletakkan. Di baris 19, program melakukan 
perhitungan matematika menggunakan operasi sisa bagi (modulo). Rumus (player_id % self.SIZE + self.SIZE) % self.SIZE ini digunakan untuk 
memastikan bahwa hasil perhitungannya selalu berupa angka yang valid di dalam rentang ukuran tabel (misalnya 0 sampai 9), sekaligus menangani 
dan menormalkan jika nilai input player_id bernilai negatif. Baris 21 mendefinisikan fungsi akun_pemain yang bertugas menyimpan data baru atau 
memperbarui data akun yang sudah ada. Pada baris 22, program memanggil fungsi self.hash_function tadi untuk mendapatkan angka posisi awal, 
lalu menyimpannya ke variabel idx. Pada baris 24, program memulai perulangan for yang akan mengecek setiap slot satu per satu sebanyak ukuran 
maksimal tabel, teknik ini digunakan untuk mencari slot kosong berikutnya jika posisi target awal sudah terisi data lain. Di baris 25, program 
menghitung variabel i sebagai indeks posisi yang sedang diperiksa saat itu. Penggunaan operasi modulo di akhir rumus ini berfungsi agar jika 
pengecekan sudah sampai di ujung akhir tabel, pencariannya bisa berputar kembali ke indeks awal tabel. Pada baris 27, program mengecek apakah 
slot di posisi i tersebut sedang dalam status terisi (SlotState.OCCUPIED). Jika ya, program masuk ke baris 28 untuk mengecek apakah player_id 
di slot tersebut sama persis dengan player_id yang ingin dimasukkan. Jika sama, artinya data akun itu sudah terdaftar, sehingga baris 29 hanya 
bertugas memperbarui teks username dengan yang baru, dan baris 30 mengembalikan nilai True sebagai tanda proses pembaruan berhasil.
Sebaliknya, pada baris 32 (else:), jika hasil pengecekan di baris 27 mendapati bahwa slot tersebut kosong, maka program akan mengeksekusi 
baris 33 dan 34 untuk mencatat data player_id dan username yang baru ke posisi tersebut. Baris 35 kemudian mengubah status slot itu menjadi 
SlotState.OCCUPIED (terisi). Setelah itu, baris 36 mengembalikan nilai True yang berarti penambahan akun baru sukses dilakukan. Terakhir, jika 
perulangan selesai dilakukan namun program melompat ke baris 38, itu berarti seluruh slot di dalam tabel sudah penuh, sehingga fungsi mengembalikan 
nilai False karena data tidak bisa ditambahkan.


<img width="1290" height="713" alt="Screenshot 2026-06-08 205307" src="https://github.com/user-attachments/assets/4abf0565-fc46-4000-9dce-b047db01be6a" />

Pada baris 40, program mendefinisikan fungsi cari_akun untuk mencari data akun berdasarkan player_id yang diberikan. Di baris 41, 
program memanggil fungsi self.hash_function untuk menghitung angka posisi awal pencarian dan menyimpannya di dalam variabel idx. 
Pada baris 43, program memulai perulangan untuk memeriksa slot satu per satu untuk mengantisipasi jika data bergeser dari posisi asalnya. 
Baris 44 menghitung indeks posisi i yang sedang diperiksa saat itu. Pada baris 46 dan 47, program mengecek apakah slot di posisi i 
berstatus kosong (SlotState.EMPTY). Jika terdeteksi kosong, proses pencarian langsung dihentikan dan fungsi mengembalikan nilai None, 
karena secara logika data yang dicari pasti tidak ada di posisi selanjutnya jika posisi saat ini sudah kosong. Pada baris 49 dan 50, 
jika slot tersebut terisi dan nilai player_id di dalamnya sama dengan yang dicari, baris 51 akan mengembalikan seluruh objek data di slot 
tersebut. Terakhir, jika seluruh perulangan tabel selesai dilakukan namun data tetap tidak ditemukan, baris 53 akan mengembalikan nilai None. 
Baris 55 mendefinisikan fungsi tampilkan_data yang bertugas membaca dan mencetak seluruh isi struktur tabel ke layar. Pada baris 56, program 
mencetak teks judul tabel. Di baris 58, program memulai perulangan for yang berjalan berurutan dari indeks ke-0 hingga batas akhir ukuran tabel. 
Pada baris 59, program mencetak angka indeks posisi saat ini. Perintah tambahan end="" di akhir instruksi cetak berfungsi agar keluaran teks 
berikutnya menyambung di sebelah kanannya, bukan turun ke baris baru. Pada baris 61 dan 62, program mengecek status slot di indeks tersebut,
jika berstatus kosong, program mencetak teks "EMPTY". Sebaliknya pada baris 64 (else:), yang berarti slot tersebut memiliki status terisi, 
program akan melompat ke baris 65 hingga 68 untuk mencetak nilai player_id dan username yang tersimpan di dalamnya.


<img width="1009" height="656" alt="Screenshot 2026-06-08 205315" src="https://github.com/user-attachments/assets/5234f5ec-9b79-44e5-b65f-395d46b6bd1a" />

Pada baris 71, program mendefinisikan fungsi main sebagai titik pusat berjalannya aplikasi. Di baris 72, program membuat objek struktur 
data baru dari kelas HashMapAkunGame dan menyimpannya di dalam variabel bernama game. Dari baris 74 hingga 77, program memanggil fungsi
game.akun_pemain sebanyak empat kali secara berurutan. Langkah ini bertujuan untuk memasukkan empat data akun sementara ke dalam tabel 
memori sebagai data awal percobaan, di mana masing-masing baris memasukkan pasangan nomor ID pemain beserta nama penggunanya (username).
Baris 79 bertugas mencetak teks judul "LOGIN GAME RPG" ke layar. Pada baris 81, program memulai instruksi perulangan while True, yang 
artinya proses di bawahnya akan terus diulang tanpa batas waktu sampai ada perintah khusus yang menghentikannya. Di baris 82, program 
meminta pengguna mengetikkan nomor ID pemain, mengubah ketikan tersebut menjadi format angka bilangan bulat (integer), dan menyimpannya 
ke variabel player_id. Pada baris 84, program memanggil fungsi pencarian game.cari_akun menggunakan nomor ID yang baru diketik tadi, 
lalu menyimpan hasil pencariannya ke dalam variabel akun. Pada baris 86, program mengecek apakah variabel akun memiliki isi data atau 
tidak bernilai None. Jika memiliki isi (berarti ID terdaftar), program mengeksekusi baris 87 dan 88 untuk mencetak pesan keberhasilan 
login yang juga menampilkan nama pengguna secara dinamis. Setelah itu, baris 89 mengeksekusi perintah break untuk memutus dan menghentikan 
perulangan while secara paksa, sehingga proses login dianggap selesai. Sebaliknya pada baris 91 (else:), jika variabel akun kosong atau 
bernilai None (berarti ID tidak ditemukan), program melompat ke baris 92 dan 93 untuk mencetak teks peringatan bahwa login gagal. Karena 
tidak ada perintah break di dalam kondisi gagal ini, program akan secara otomatis mengulang kembali prosesnya ke baris 82, yaitu meminta 
pengguna memasukkan nomor ID lagi. Baris 96 memuat kondisi standar pada struktur bahasa pemrograman Python, yaitu if __name__ == "__main__":. 
Baris ini bertugas memastikan bahwa kode di bawahnya hanya akan dieksekusi apabila file program ini dijalankan secara langsung sebagai 
skrip utama, bukan diimpor sebagai modul ke file lain. Jika syarat tersebut terpenuhi, baris 97 akan memanggil fungsi main() untuk mulai 
menjalankan seluruh urutan logika yang telah dijelaskan di atas.


**D. Output:**
<img width="1379" height="277" alt="Screenshot 2026-06-08 211016" src="https://github.com/user-attachments/assets/1c0297ce-19f6-4846-8533-4e1d09513652" />

Saat program pertama kali dijalankan, layar langsung menampilkan teks judul "===== LOGIN GAME RPG =====" dan meminta pengguna 
memasukkan angka melalui teks "Masukkan Player ID: ". Pada percobaan pertama, angka yang diketikkan adalah 1234. Karena ID 1234 
tidak ada di dalam daftar akun yang sudah didaftarkan pada kode awal, program menampilkan teks "=== LOGIN GAGAL ===" beserta pesan 
bahwa Player ID tidak ditemukan. Karena program dirancang untuk terus mengulang jika terjadi kegagalan login, layar kembali memunculkan 
teks permintaan input Player ID. Pada percobaan kedua, angka yang diketikkan adalah 1001. Karena ID 1001 tersebut sudah terdaftar 
di dalam sistem, program langsung merespons dengan menampilkan teks "=== LOGIN BERHASIL ===". Terakhir, program mencetak teks sapaan 
yang menyertakan nama pengguna (username) dari ID tersebut, yaitu "ShadowHunter", sebelum akhirnya perulangan dihentikan dan program selesai berjalan sepenuhnya.


**E. Link Youtube:** https://youtu.be/SQz19v9gkkQ



