**A. Judul Program:** Simulasi Papan Skor Game Arcade

**B. Deskripsi Singkat:**
Program ini mensimulasikan papan skor game arcade menggunakan struktur data Binary Search Tree (BST). 
Setiap pemain dicatat nama dan skornya. Skor dijadikan kunci (key) BST dan nantinya data otomatis tersusun dari terendah ke tertinggi (inorder).

**C. Source Code:**

<img width="1088" height="638" alt="image" src="https://github.com/user-attachments/assets/74b1b86c-88f8-4396-b455-d5791477dce2" />

Pada baris 1, program mendefinisikan sebuah kelas bernama Node. Baris 2 adalah fungsi __init__ yang otomatis berjalan ketika objek Node baru dibuat. 
Baris 3 dan 4 berfungsi untuk menyimpan nilai skor dan nama ke dalam objek tersebut. Selanjutnya, baris 5 dan 6 membuat variabel self.left dan 
self.right yang diisi dengan nilai None. Kedua variabel ini disiapkan untuk menyimpan referensi ke objek Node lainnya di sebelah kiri dan kanan pada struktur data nanti.
Pada baris 9, program mendefinisikan kelas bernama ArcadeBST. Baris 10 merupakan fungsi __init__ untuk menginisialisasi kelas tersebut saat digunakan. 
Di baris 11, program membuat variabel self.root dan menetapkan nilainya menjadi None. Ini berarti struktur Binary Search Tree (BST) belum memiliki data
apa pun pada saat pertama kali dibuat. Baris 13 mendefinisikan fungsi insert untuk memproses penambahan data. Pada baris 14 dan 15, program mengecek 
apakah posisi root saat ini bernilai None. Jika ya, program akan membuat dan mengembalikan objek Node baru berisi data skor dan nama. Jika tidak bernilai None, 
baris 16 dan 17 mengecek apakah skor baru lebih kecil dari skor saat ini. jika ya, fungsi insert dipanggil kembali untuk memproses variabel left. 
Sebaliknya pada baris 18 dan 19, jika skor baru lebih besar, fungsi insert dipanggil kembali untuk memproses variabel right. Baris 20 dan 21 menangani 
kondisi jika skor yang dimasukkan sama persis dengan yang sudah ada, dengan mencetak teks bahwa skor sudah ada. Terakhir, baris 22 mengembalikan nilai root 
agar struktur data tetap tersambung. Baris 24 mendefinisikan fungsi tambah_skor yang dipanggil ketika pengguna ingin memasukkan data. Pada baris 25, fungsi ini 
memperbarui nilai self.root dengan mengeksekusi fungsi self.insert, di mana prosesnya selalu dimulai dari self.root saat itu. Terakhir, baris 26 mencetak teks 
konfirmasi ke layar yang menginformasikan bahwa skor dan nama telah berhasil ditambahkan.


<img width="1089" height="475" alt="image" src="https://github.com/user-attachments/assets/b5515bc4-7856-4d20-a104-a5100a1b313b" />

Pada baris 28, program mendefinisikan fungsi search yang bertugas mencari data skor tertentu di dalam struktur yang sudah ada. Di baris 29 dan 30, 
program memeriksa apakah posisi yang sedang dicek bernilai None. Jika ya, program mengembalikan nilai None yang berarti pencarian telah mencapai 
ujung dan data tidak ditemukan. Pada baris 31 dan 32, program mengecek apakah skor pada posisi saat ini sama dengan skor yang dicari. Jika cocok, 
program akan langsung mengembalikan data tersebut. Jika belum cocok, baris 33 dan 34 akan mengecek apakah skor yang dicari lebih kecil. Jika lebih kecil, 
pencarian diteruskan ke cabang sebelah kiri (root.left). Sebaliknya di baris 35, jika skor yang dicari lebih besar, pencarian diteruskan ke cabang 
sebelah kanan (root.right). Baris 37 mendefinisikan fungsi cari_skor, yaitu fungsi yang akan dipanggil oleh pengguna saat ingin mencari skor. 
Pada baris 38, program menjalankan perintah pencarian dengan memanggil fungsi self.search yang prosesnya dimulai dari data paling atas (self.root), 
lalu menyimpan hasil pencarian tersebut ke dalam variabel bernama node. Di baris 39 dan 40, program memeriksa hasil pencariannya. Jika node berisi data, 
program akan menampilkan pesan nama pemain beserta skornya. Sebaliknya pada baris 41 dan 42, jika node bernilai kosong atau None, 
program akan menampilkan pesan bahwa skor tersebut tidak ditemukan. Baris 44 mendefinisikan fungsi find_min_node yang berfungsi khusus untuk mencari data 
dengan nilai skor paling rendah. Pada baris 45, program menggunakan loop while yang akan terus bekerja selama posisi sebelah kiri (root.left) 
masih memiliki data. Di dalam loop tersebut pada baris 46, program akan terus memindahkan fokus pengecekan ke arah kiri secara berulang kali. 
Ketika sudah mencapai ujung paling kiri dan perulangan berhenti, baris 47 akan mengembalikan data yang berada di posisi terakhir tersebut, 
karena posisi paling kiri selalu menyimpan nilai yang paling kecil.


<img width="1228" height="741" alt="Screenshot 2026-05-21 103234" src="https://github.com/user-attachments/assets/8cf230be-0799-4633-bcdd-4e7716cae503" />

Pada baris 49, program mendefinisikan fungsi delete untuk memproses penghapusan data dari struktur. Pada baris 50 dan 51, program mengecek 
apakah posisi bernilai None. Jika ya, fungsi mengembalikan nilai None karena data tidak ada. Baris 52 hingga 55 berfungsi mencari data yang ingin dihapus. 
Jika skor lebih kecil, pencarian diteruskan ke cabang kiri (root.left), dan jika lebih besar, ke cabang kanan (root.right). Jika data yang dicari ditemukan, 
baris 56 (else:) akan mengeksekusi penghapusan yang terbagi dalam tiga kondisi:
1. Baris 57-58: Jika data tidak memiliki cabang di sebelah kiri, posisi tersebut akan langsung digantikan oleh data dari cabang kanannya.
2. Baris 59-60: Sebaliknya, jika data tidak memiliki cabang di sebelah kanan, posisi tersebut akan digantikan oleh data dari cabang kirinya.
3. Jika data memiliki cabang di kiri dan kanan, program tidak bisa langsung menghapusnya. Pada baris 61, program mencari data pengganti dengan 
nilai terkecil di cabang sebelah kanan menggunakan fungsi find_min_node. Di baris 62 dan 63, skor dan nama dari data terkecil tersebut disalin 
untuk menimpa data yang ingin dihapus. Terakhir, di baris 64, data terkecil yang asli tadi dihapus dari posisi asalnya di cabang kanan.

Baris 67 mendefinisikan fungsi hapus_skor yang dipanggil pengguna saat ingin menghapus data. Di baris 68, program memanggil fungsi self.search terlebih 
dahulu untuk memastikan skor yang ingin dihapus benar-benar terdaftar di dalam sistem. Jika skor tersebut ditemukan, baris 69 akan memperbarui self.root 
dengan mengeksekusi fungsi self.delete untuk menghapus datanya. Baris 70 kemudian menampilkan pesan bahwa penghapusan berhasil. Jika pada baris 68 skor tidak 
ditemukan, program akan melompat ke baris 71 dan 72 untuk menampilkan pesan bahwa skor tidak ditemukan. Baris 74 mendefinisikan fungsi inorder yang bertugas 
membaca dan menampilkan seluruh data secara berurutan dari skor terkecil hingga terbesar. Pada baris 75 dan 76, jika posisi yang dibaca bernilai None, proses 
pembacaan untuk jalur tersebut dihentikan. Di baris 77, program memanggil fungsi inorder itu sendiri secara terus-menerus untuk turun ke cabang paling kiri, 
karena posisi kiri menyimpan nilai-nilai terkecil. Setelah mencapai ujung kiri, baris 78 akan menampilkan pesan skor dan nama ke layar. Setelah itu, baris 79 
menyuruh program untuk bergeser membaca cabang sebelah kanan. Urutan pengerjaan ini (kiri, cetak, kanan) memastikan data selalu keluar secara berurutan.


<img width="1210" height="761" alt="image" src="https://github.com/user-attachments/assets/a4b3e98a-9c1b-4e8f-bc09-305c61400625" />

Pada baris 81, program mendefinisikan fungsi tampilkan_papan_skor untuk mencetak seluruh isi papan peringkat ke layar. Baris 82 memeriksa 
apakah self.root bernilai None. Jika iya, yang berarti belum ada data sama sekali, baris 83 akan mencetak teks "Belum ada skor." dan baris 84 
akan menghentikan eksekusi fungsi tersebut menggunakan instruksi return. Jika data sudah tersedia, baris 85 dan 86 bertugas mencetak judul kolom 
berupa teks "Skor" dan "Nama" beserta garis pembatas di bawahnya. Kemudian pada baris 87, program memanggil fungsi self.inorder yang prosesnya 
dimulai dari self.root untuk menampilkan seluruh data secara berurutan. Baris 89 mendefinisikan fungsi skor_terendah untuk mencari dan menampilkan 
skor paling kecil. Baris 90 hingga 92 memiliki fungsi yang sama seperti sebelumnya, yaitu mengecek apakah struktur data masih kosong. Jika kosong, 
program mencetak "Belum ada skor." lalu berhenti bekerja. Jika ada isinya, baris 93 memanggil fungsi self.find_min_node yang akan mencari dan 
mengembalikan data dengan nilai terkecil, kemudian menyimpan hasilnya di dalam variabel bernama node. Baris 94 kemudian menampilkan skor dan nama 
yang diambil dari variabel node tersebut. Baris 96 mendefinisikan fungsi skor_tertinggi untuk mencari skor paling besar. 
Setelah pengecekan kekosongan data di baris 97 hingga 99, program membuat variabel current pada baris 100 yang diisi dengan posisi awal (self.root). 
Baris 101 adalah loop while yang akan terus berjalan selama cabang sebelah kanan (current.right) memiliki data atau tidak bernilai None. Di dalam 
loop tersebut pada baris 102, fokus pengecekan terus digeser ke arah kanan (current.right). Karena aturan struktur data ini menempatkan nilai terbesar 
di ujung paling kanan, perulangan ini memastikan program mencapai titik tersebut. Setelah perulangan berhenti di ujung kanan, baris 103 mencetak skor
dan nama dari posisi terakhir itu. Pada baris 105, program mendefinisikan fungsi count_nodes yang bertugas menghitung jumlah total data di dalam sistem.
Di baris 106 dan 107, jika posisi yang sedang dicek bernilai None, fungsi akan mengembalikan angka 0. Jika posisinya memiliki data, baris 108 akan 
melakukan perhitungan: angka 1 (yang mewakili data di posisi saat itu) ditambahkan dengan total perhitungan dari seluruh cabang sebelah kiri, lalu 
ditambahkan lagi dengan total perhitungan dari seluruh cabang sebelah kanan. Fungsi ini memanggil dirinya sendiri berulang kali untuk menelusuri dan 
menjumlahkan semua sisi struktur data. Baris 110 mendefinisikan fungsi total_pemain yang merupakan fungsi praktis untuk dipanggil oleh pengguna saat 
ingin melihat jumlah pemain. Pada baris 111, program menampilkan teks "Total pemain:" yang kemudian langsung digabungkan dengan hasil angka dari pemanggilan 
fungsi self.count_nodes(self.root).


<img width="1090" height="596" alt="image" src="https://github.com/user-attachments/assets/36286988-586a-4616-8609-70287cf0ab17" />

Pada baris 113, program mendefinisikan fungsi find_successor untuk mencari data dengan nilai skor tepat satu tingkat di atas skor 
yang diberikan. Baris 114 hingga 116 menyiapkan nilai awal. Variabel current diisi dengan posisi awal pencarian (root), successor
disiapkan dengan nilai None untuk menyimpan hasil akhir, dan found diisi False sebagai penanda apakah skor target ada di dalam sistem. 
Pada baris 117, perulangan while terus berjalan selama variabel current masih memiliki data. Di baris 118 hingga 120, jika skor target 
lebih kecil dari skor yang sedang dicek, program mencatat posisi saat ini ke dalam variabel successor sebagai calon jawaban, lalu menggeser 
pencarian ke cabang sebelah kiri (current.left). Pada baris 121 dan 122, jika skor sasaran lebih besar, pencarian langsung digeser ke cabang
sebelah kanan (current.right). Baris 123 menangani kondisi ketika skor sasaran persis sama dengan skor yang sedang dicek. Pada baris 124,
status found diubah menjadi True karena datanya sudah ditemukan. Di baris 125 dan 126, program mengecek apakah ada data di cabang sebelah kanan. 
Jika ada, nilai successor akan diperbarui dengan mengambil nilai paling kecil dari cabang kanan tersebut menggunakan fungsi self.find_min_node. 
Baris 127 menghentikan perulangan pencarian. Terakhir, baris 128 mengembalikan nilai variabel successor beserta status found.
Baris 130 mendefinisikan fungsi skor_diatas yang dapat dipanggil pengguna untuk mencari data dengan skor tepat di atas skor yang dimasukkan. 
Pada baris 131, program memanggil fungsi self.find_successor yang telah dijelaskan sebelumnya, kemudian menyimpan data yang dikembalikan ke dalam 
variabel node dan status penemuannya ke dalam variabel found. Pada baris 132 dan 133, jika status found bernilai salah atau False, program akan 
menampilkan pesan bahwa skor tersebut tidak ditemukan di dalam sistem. Pada baris 134 dan 135, jika variabel node memiliki isi data, itu berarti 
skor di atasnya berhasil ditemukan, lalu program akan menampilkan nilai skor beserta nama pemainnya ke layar. Terakhir, baris 136 dan 137 menangani 
kondisi sisa, yaitu ketika skor sasaran ada di dalam sistem tetapi variabel node bernilai None (tidak ada skor yang lebih besar), sehingga 
program menampilkan pesan bahwa skor yang dimasukkan adalah skor tertinggi.


<img width="1007" height="856" alt="image" src="https://github.com/user-attachments/assets/1f36dd54-18da-4f63-880b-5f75252124e6" />

Pada baris 140, program mendefinisikan fungsi main yang merupakan fungsi utama untuk menjalankan seluruh program ini. 
Di baris 141, program membuat struktur data baru dengan memanggil cetakan ArcadeBST dan menyimpannya ke dalam variabel bst.
Baris 142 membuat variabel pilih dan memberikan nilai awal 0. Pada baris 144, program memulai perulangan while yang akan 
terus berjalan dan menampilkan menu selama nilai variabel pilih tidak sama dengan angka 9. Selanjutnya, baris 145 hingga 154
adalah barisan kode untuk mencetak teks ke layar, yang menampilkan judul dan sembilan opsi menu untuk dipilih oleh pengguna.
Baris 156 memulai blok try untuk menangani kemungkinan terjadinya program terhenti (error) akibat typo dari pengguna. 
Pada baris 157, program meminta pengguna mengetikkan angka pilihan dengan tipe data integer (bilangan  bulat), dan menyimpannya 
ke dalam variabel pilih. Jika pengguna mengetikkan selain integer, baris 159 kemudian akan menampilkan pesan "Input tidak valid!", 
dan baris 160 (continue) menginstruksikan program untuk kembali langsung ke awal perulangan pada baris 144. 
Pada baris 162, program mengecek apakah nilai variabel pilih adalah 1. Jika benar, program masuk ke blok try di baris 163. 
Pada baris 164, program meminta pengguna memasukkan angka skor. Di baris 165, program meminta input nama pemain. 
.strip() di akhir digunakan untuk menghapus spasi kosong yang mungkin tidak sengaja terketik di awal atau akhir nama. Pada baris 166, 
program memanggil fungsi bst.tambah_skor untuk memasukkan data yang baru saja diketik ke dalam sistem pencatatan. Jika pada tahap ini 
pengguna memasukkan huruf saat diminta memasukkan skor, baris 168 akan menampilkan pesan "Input tidak valid!". 
Baris 170 mengecek apakah variabel pilih bernilai 2. Jika benar, program kembali masuk ke blok penanganan try di baris 171. Pada baris 172, 
program meminta pengguna untuk memasukkan skor target yang ingin dicari, dengan ketentuan format berupa angka bilangan bulat. Di baris 173, 
program memanggil fungsi bst.cari_skor untuk mencari skor tersebut di dalam struktur data yang ada. Sama seperti sebelumnya, except ValueError 
akan terjadi jika tipe data yang diinputkan tidak sesuai. 


<img width="1027" height="733" alt="image" src="https://github.com/user-attachments/assets/211a6356-adf3-4463-a093-e8ece84172b3" />

Pada baris 177, program mengecek apakah pengguna memilih angka 3. Jika ya, program masuk ke blok penanganan try di baris 178. 
Pada baris 179, program meminta pengguna memasukkan angka skor yang ingin dihapus. Baris 180 kemudian memanggil fungsi bst.hapus_skor 
untuk menghapus skor tersebut dari dalam struktur data. Jika pengguna memasukkan huruf atau karakter selain angka pada saat input, baris 
181 dan 182 akan menangkap kesalahan format tersebut lalu mencetak teks "Input tidak valid!".
Bagian ini menangani pemanggilan fungsi secara langsung berdasarkan pilihan menu yang dieksekusi tanpa memerlukan input tambahan. 
Pada baris 184 dan 185, jika pilihan adalah 4, program memanggil fungsi bst.tampilkan_papan_skor() untuk mencetak seluruh isi data ke layar. 
Pada baris 187 dan 188, jika pilihan adalah 5, program memanggil fungsi bst.skor_terendah() untuk menampilkan data dengan skor paling kecil. 
Pada baris 190 dan 191, jika pilihan adalah 6, program memanggil fungsi bst.skor_tertinggi() untuk menampilkan data dengan skor paling besar. 
Selanjutnya pada baris 193 dan 194, jika pilihan adalah 7, program memanggil fungsi bst.total_pemain() untuk menghitung dan menampilkan 
jumlah seluruh pemain yang terdaftar.
Pada baris 196, program mengecek apakah pilihan bernilai 8. Jika benar, program kembali masuk ke blok try di baris 197. Baris 198 meminta 
pengguna untuk memasukkan angka key. Selanjutnya pada baris 199, program memanggil fungsi bst.skor_diatas untuk mencari nilai yang posisinya 
berada tepat satu tingkat di atas skor key tersebut. Baris 200 dan 201 berfungsi sama seperti pada pilihan-pilihan sebelumnya, yaitu jika 
pengguna memasukkan teks biasa ke dalam fungsi input angka, lalu menampilkan pesan tidak valid.
Pada baris 203, program mengecek apakah pengguna memilih angka 9. Jika ya, baris 204 akan mengeksekusi perintah untuk menampilkan teks 
"Game over!". Pilihan angka 9 ini juga berfungsi untuk menghentikan loop utama program yang sudah didefinisikan di awal. Terakhir, baris 
206 dan 207 memuat instruksi else, jika pengguna menginputkan angka di luar rentang 1 sampai 9, baris 207 akan mencetak teks "Pilihan tidak valid!"
dan program kembali menampilkan menu awal.


**D. Output:**

<img width="931" height="647" alt="image" src="https://github.com/user-attachments/assets/e3eab803-1d27-40d5-a268-d8857638ed92" />
<img width="784" height="612" alt="image" src="https://github.com/user-attachments/assets/76231154-fb54-4f06-91ab-dfc55b8a33e6" />
<img width="824" height="659" alt="image" src="https://github.com/user-attachments/assets/8ebb227f-a4e3-4247-adb1-d0bafc4c6055" />
<img width="1166" height="897" alt="image" src="https://github.com/user-attachments/assets/60d0a6a3-e0e4-441d-9b69-7832b7562f49" />
<img width="1156" height="910" alt="image" src="https://github.com/user-attachments/assets/0111625c-f1c7-46ca-9f9a-70d5e0f312f6" />
<img width="649" height="261" alt="image" src="https://github.com/user-attachments/assets/f63da465-2d89-4f8a-a6a8-ef4da0919c58" />

Pada saat program pertama kali dijalankan, pengguna memilih opsi nomor 1 (Tambah skor) sebanyak tiga kali. Pengguna secara berurutan 
memasukkan skor 5 dengan nama "ela", skor 3 dengan nama "eli", dan skor 7 dengan nama "elo". Setiap penambahan data selalu diikuti 
dengan pesan bahwa data berhasil ditambahkan. Setelah ketiga data masuk, pengguna memilih opsi nomor 7 (Total pemain), dan program 
secara akurat menampilkan angka 3, yang menunjukkan ada tiga data pemain yang tersimpan di dalam sistem. Selanjutnya, pengguna memilih 
opsi nomor 4 (Tampilkan papan skor). Program menampilkan ketiga data yang sudah dimasukkan sebelumnya dalam bentuk daftar yang otomatis 
terurut dari skor terkecil ke terbesar, yaitu mulai dari 3 (eli), 5 (ela), hingga 7 (elo). Kemudian, pengguna memilih opsi nomor 5 
(Skor terendah) dan opsi nomor 6 (Skor tertinggi). Program merespons dengan benar dengan menampilkan skor 3 milik "eli" sebagai skor 
paling rendah, dan skor 7 milik "elo" sebagai skor paling tinggi. Pengguna lalu melanjutkan dengan memilih opsi nomor 2 (Cari skor) untuk 
mencari keberadaan skor 5. Program memproses input tersebut dan menampilkan informasi bahwa skor 5 ditemukan atas nama "ela". Setelah itu,
pengguna menggunakan opsi nomor 3 (Hapus skor) dan memasukkan angka 7 sebagai data yang ingin dihapus. Program mengonfirmasi bahwa skor 7 
berhasil dihapus, yang berarti data milik "elo" sekarang sudah tidak ada lagi. Lalu, pengguna memilih opsi nomor 8 (Skor tepat di atas nilai tertentu) 
sebanyak tiga kali. Percobaan pertama mencari skor di atas angka 3, program mengembalikan skor 5 milik "ela" karena itu adalah angka terdekat di atas 3. 
Percobaan kedua mencari skor di atas angka 7, program menampilkan pesan bahwa skor 7 tidak ditemukan, karena data tersebut sudah dihapus pada langkah sebelumnya. 
Percobaan ketiga mencari skor di atas angka 5, karena skor 7 sudah terhapus, skor 5 saat ini otomatis menjadi skor terbesar di dalam sistem, sehingga 
program menampilkan pesan bahwa 5 adalah skor tertinggi dan tidak ada angka lagi di atasnya. Terakhir, pengguna memilih opsi nomor 9 (Keluar). 
Program merespons dengan menampilkan teks "Game over!" , yang menandakan bahwa loop fungsi utama telah dihentikan dan seluruh jalannya program telah ditutup.


**E. Link Youtube:** https://youtu.be/8V4dUNsOtZI



