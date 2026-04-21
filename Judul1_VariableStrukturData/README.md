Judul Program: Game Rantai Kata Menggunakan Linked List

Deskripsi Singkat:
Program ini merupakan implementasi dari struktur data linked list, di mana user dapat menginputkan kata pertama secara bebas lalu kata selanjutnya harus menggunakan
huruf terakhir dari kata sebelumnya. Jika user tidak memilih kata yang berawalan huruf terakhir dari kata sebelumnya, program akan menolak kata tersebut dan 
meminta user menggunakan kata lain, begitu pula jika user menginputkan kata yang sama seperti kata yang sudah pernah diinputkan sebelumnya, maka program akan
menolak kata tersebut. Karena menggunakan linked list, kata yang diinputkan user akan tersimpan di node-node di mana tiap node memiliki pointer yang menunjuk ke 
node selanjutnya.

Source Code:
<img width="1182" height="665" alt="image" src="https://github.com/user-attachments/assets/32f00443-ce30-4cce-a12c-c8539d9484cf" />

Bagian kode pada gambar ini menggunakan struktur data linked list. Di baris pertama, dibuat kelas Node yang berfungsi sebagai tempat untuk menyimpan satu kata 
dan pointer ke node selanjutnya. Selanjutnya ada kelas RantaiKata yang fungsinya untuk mengatur permainan. Di dalamnya ada variabel head untuk menyimpan kata 
pertama dan rear untuk menyimpan kata terakhir. Program ini juga memiliki fungsi tambah_kata() yang digunakan untuk menambahkan kata baru ke dalam rantai. Saya 
di sini menggunakan lower() agar kata yang diamsukkan konsisten menggunakan huruf kecil agar sistem tidak bingung. Kalau rantai masih kosong, kata yang diinputkan 
akan menjadi kata pertama. Namun jika sudah ada kata sebelumnya, program akan mengecek apakah kata tersebut sudah pernah digunakan atau belum, jika sudah maka 
program akan menolak kata tersebut. 


<img width="1402" height="618" alt="image" src="https://github.com/user-attachments/assets/ee0525fe-c420-4aec-bc52-5d56322314e6" />

Pada bagian kode ini, program mengecek apakah kata baru dapat disambungkan ke rantai kata yang sudah ada. Program mengambil huruf terakhir dari kata terakhir dalam
rantai dan huruf pertama dari kata baru yang diinputkan user. Jika kedua huruf itu sama, maka program membuat node baru untuk menyimpan kata tersebut, kemudian 
kata itu dihubungkan ke node terakhir, jadi node bertambah panjang. Tapi, jika huruf pertama kata baru tidak sama dengan huruf terakhir kata sebelumnya, maka kata itu 
tidak bisa ditambahkan dan program akan menampilkan pesan bahwa kata tidak dapat disambung. Lalu ada fungsi tampilkan_rantai() yang digunakan untuk menampilkan semua 
kata yang sudah diinputkan oleh user. Jika user belum menginputkan apa-apa maka akan tampil pesan bahwa rantai masih kosong. Jika sudah ada, maka program akan membaca 
setiap node dari kata pertama hingga terakhir, lalu disimpan secara sementara dalam sebuah list. Setelah semua kata terkumpul, proram menampilkan seluruh kata tersebut 
secara berurutan dengan tanda panah (->).


<img width="1076" height="494" alt="image" src="https://github.com/user-attachments/assets/65a92fac-d21e-4515-b60a-be2e6e4e9105" />

Pada bagian ini, program mulai menjalankan game rantai kata. Pertama, program membuat objek game dari kelas RantaiKata, setelah itu program menampilkan judul game
serta bertanya pada user untuk mengetik 'keluar' untuk berhenti atau 'mulai' untuk bermain. Program menggunakan loop while True supaya pengguna bisa terus memasukkan 
kata, lalu mengecek apakah pengguna mengetik 'keluar' atau 'mulai'. Jika pengguna memasukkan kata biasa, maka kata itu diproses oleh fungsi tambah_kata() untuk dicek 
apakah bisa disambungkan ke rantai kata. Setelah pengguna keluar dari game, program menampilkan pesan bahwa game telah berakhir dan menampilkan hasil akhir dari rantai
kata yang sudah berhasil dibuat.


Output Program:
<img width="1541" height="601" alt="Screenshot 2026-04-21 115400" src="https://github.com/user-attachments/assets/7196f619-1f1c-4f4d-8ba2-478dc2fdde92" />

Gambar ini merupakan output dari source code di atas. Di baris pertama, program menunjukkan judul game lalu memberikan opsi pada user untuk mengetik 'keluar' atau 'mulai'. 
Di gambar ini, user memilih untuk mengetik 'mulai', dan program memberikan pesan bahwa rantai masih kosong, dan meminta user menginputkan sebuah kata. User menginputkan kata 
'pisang' dan program menampilkan pesan 'Kata pertama pisang berhasil ditambahkan'. Lalu user dapat menginputkan kata selanjutnya yang huruf awalnya harus sama seperti huruf
terakhir dari kata sebelumnya, jadi ia menginputkan kata 'gorengan' sehingga program menampilkan pesan 'kata 'gorengan' berhasil disambung'. User menginputkan kata ketiga, 
namun di sini user menginputkan kata yang huruf awalnya tidak sama seperti huruf terakhir kata sebelumnya, yaitu 'mangga', sehingga program menampilkan pesan 'kata mangga 
tidak bisa disambung, huruf awal 'm' tidak sama dengan huruf akhir 'n'. Jadi, user mengganti kata tersebut dan menginputkan 'nasi'. Sistem menerima kata tersebut. User ingin 
berhenti bermain, jadi ia mengetik kata 'keluar' bukan menginputkan kata selanjutnya. Jadi, sistem menampilkan pesan bahwa game telah berakhir dan juga menampilkan
rantai kata yang telah dibuat.
Output: pisang->gorengan->nasi

Link Youtube: https://youtu.be/-dDL2tkuM-Q 
