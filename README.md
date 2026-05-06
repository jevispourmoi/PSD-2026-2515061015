**A. Judul Program** 
Pencarian Posisi Buku di Perpustakaan

**B. Deskripsi Singkat** 
Program ini mengimplementasikan algoritma sequential search, di mana program ini dimiliki oleh sebuah perpustakaan untuk membantu pengunjung menemukan posisi
buku yang dicari. Jadi, pengunjung atau pengguna bisa menginputkan judul buku sesuai dengan daftar buku yang ditampilkan, dan program akan menunjukkan posisi
di mana buku tersebut berada.

**C. Source Code**

<img width="944" height="290" alt="image" src="https://github.com/user-attachments/assets/2a34a3ae-a6b5-42aa-b860-5bc84227da3d" />

Fungsi sequential_search(data_buku, n, target) ini tugasnya mencari judul buku di dalam list. Pertama, i = 0 artinya pencarian dimulai dari buku pertama 
(indeks 0). Lalu pos = -1 adalah nilai awal yang artinya "belum ditemukan". Kemudian while i < n adalah perulangan yang terus berjalan selama i belum 
melewati buku terakhir. Di dalam perulangan, if data_buku[i] == target mengecek apakah judul buku pada posisi i sama dengan judul yang dicari. 
Kalau sama, pos = i menyimpan posisi buku tersebut, lalu break menghentikan pencarian karena bukunya sudah ketemu. Kalau belum sama, i += 1 memindah 
pencarian ke buku berikutnya. Setelah perulangan selesai, return pos mengembalikan posisi buku, kalau ketemu berisi angka indeksnya, kalau tidak ketemu tetap -1.


<img width="1417" height="875" alt="image" src="https://github.com/user-attachments/assets/b04e6785-2c42-4529-9292-8951a92ae455" />

Fungsi main() ini adalah bagian utama yang dijalankan saat program dibuka. data_buku adalah list yang berisi 10 judul buku yang bisa dicari oleh pengguna. rak adalah list 
terpisah yang menyimpan lokasi rak dari masing-masing buku — indeksnya sengaja dibuat sama persis dengan data_buku, jadi buku di indeks ke-0 ada di rak indeks ke-0 juga. 
n = len(data_buku) menghitung berapa total buku yang ada. Lalu for i, judul in enumerate(data_buku) menampilkan semua judul buku ke layar satu per satu beserta nomornya, 
tapi tanpa info raknya supaya pengguna benar-benar harus mencari. Loop while True membuat program terus meminta input sampai pengguna mengetik "keluar", yang mana kondisi 
if target.lower() == "keluar" akan mendeteksinya dan break menghentikan program. Kalau bukan "keluar", pos = sequential_search(data_buku, n, target) memanggil fungsi pencarian tadi. 
Jika pos != -1 artinya buku ditemukan, maka print(f"Buku {target} ditemukan di {rak[pos]}") menampilkan lokasi raknya menggunakan indeks yang didapat. Kalau pos masih -1, 
artinya buku tidak ada dalam daftar dan program menampilkan pesan tidak ditemukan.


**D. Output**

<img width="1521" height="839" alt="Screenshot 2026-05-06 194252" src="https://github.com/user-attachments/assets/fabb551c-af8e-4f27-a9d8-2194875761e0" />

Ini adalah output dari kode di atas. Pada awalnya, program akan langsung menampilkan sepuluh daftar judul buku yang tersedia. Setelah itu, pengguna atau pengunjung
diminta untuk mengetikkan judul buku yang ingin dicari. Ketika mengetik "Teknik Digital" dengan ejaan dan huruf besar yang sama persis seperti di daftar, program 
berhasil menemukannya dan langsung memberi tahu bahwa buku tersebut tersimpan di Rak C1. Namun, saat pengguna mencoba mengetik ulang dengan tulisan "Teknik digital" 
memakai huruf 'd' kecil, program tidak dapat menemukan buku tersebut. Ini terjadi karena pemakaian huruf besar dan huruf kecil harus benar-benar sama persis seperti di daftar
agar dianggap cocok. Terakhir, kalau sudah selesai mencari dan ingin menutup programnya, pengguna tinggal mengetik perintah "keluar". Berbeda dengan saat mencari judul buku tadi, 
pengguna bebas mengetiknya dengan huruf besar ataupun kecil, contohnya seperti "KeLuaR" di percobaan kedua, dan program akan tetap mengerti lalu otomatis berhenti bekerja, ini terjadi karena kode if target.lower() == "keluar".

**Link Youtube**
https://youtu.be/uwAuyxnkjCY
