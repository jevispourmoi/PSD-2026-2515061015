**A. Judul Program  :** Daftar Produk Toko

**B. Deskripsi Singkat :**
Program ini adalah program untuk mengurutkan daftar produk di sebuah toko berdasarkan harga, dari yang termurah sampai yang termahal.
Pengguna bisa memasukkan beberapa produk beserta harganya, lalu program akan menampilkan daftar produk sebelum dan sesudah diurutkan.
Algoritma yang digunakan adalah selection sort, yaitu salah satu algoritma sorting yang cara kerjanya dengan mencari elemen terkecil 
dari data yang belum terurut, lalu menukarnya ke posisi yang seharusnya. Proses ini diulang terus sampai semua data sudah tersusun rapi.

**C. Source Code :**

<img width="1171" height="394" alt="Screenshot 2026-04-30 112952" src="https://github.com/user-attachments/assets/915daca5-07a8-4377-8632-2dda9a15ca6d" />

Fungsi tukar() berfungsi untuk menukar posisi produk dalam list. Caranya adalah dengan variabel temp sebagai penyimpanan nilai sementara
agar nilai pertama tidak hilang. Jadi urutan prosesnya adalah menyimpan nilai arr[i] ke temp, isi arr[i] dengan nilai arr[j], setelah itu 
isi arr[j] dengan nilai yang disimpan di temp. Sedangkan fungsi selection_sort() adalah inti program. Ada dua loop yang berjalan. Loop for i
berjalan dari awal sampai hampir akhir list, tugasnya menentukan posisi mana yang mau diisi. Loop for j bertugas untuk mencari produk dengan 
harga paling murah (nilai minimum) dari list yang belum terurut. Kalau ketemu yang lebih murah, simpan posisinya di variabel pos. Setelah
loop selesai, kalau ternyata posisi terkecil (pos) bukan di posisi sekarang (i), maka posisi akan ditukar dengan fungsi tukar(). Begitu terus
sampai semua produk terurut. 


<img width="1304" height="773" alt="Screenshot 2026-04-30 113004" src="https://github.com/user-attachments/assets/3234a7d2-d089-4f22-8858-e29d889c2fea" />

Fungsi main() merupakan fungsi utama yang mengatur jalannya program dari awal sampai akhir. Pertama, program akan meminta input jumlah produk 
dengan try-except, jadi kalau pengguna salah dan bukan menginputkan integer, maka program tidak akan crash. Setelah itu, program akan meminta 
input nama dan harga tiap produk satu per satu, dan disimpan dalam bentuk dictionary, yang dikumpulkan pada list arr. Inputan harga menggunakan 
loop while True supaya kalau salah input bisa diulang. Setelah semua data masuk, program tampilkan daftar produk sebelum diurutkan, lalu panggil
selection_sort() dan akan menampilkan lagi hasil yang telah diurutkan.

**D. Ouput Program :**

<img width="1536" height="534" alt="Screenshot 2026-04-30 113056" src="https://github.com/user-attachments/assets/c5007cc9-b2b6-4f86-ad02-d33d585f27e3" />

Setelah program dijalankan, pengguna diminta memasukkan jumlah produk dan data tiap produk (nama+harga). Program kemudian menampilkan dua daftar, 
yaitu daftar produk dalam urutan asli saat diinput, dan daftar produk setelah diurutkan dari harga termurah ke termahal menggunakan selection sort.
Jadi, sesuai dengan gambar, pengguna menginputkan 3 jumlah produk, yaitu kopi dengan harga 10000, teh 5000, dan susu 7000. Setelah itu, program akan 
menampilkan data produk sesuai dengan urutan saat diinputkan, lalu di bawahnya ditampilkan lagi daftar produk setelah diurutkan sesuai dari harga 
termurah hingga harga termahal. 

**E. Link Youtube :** https://youtu.be/LzZkx4fA3f8
