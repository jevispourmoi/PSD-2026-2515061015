class Node:
    def __init__(self, kata):
        self.kata = kata
        self.next = None

class RantaiKata:
    def __init__(self):
        self.head = None
        self.rear = None

    def tambah_kata(self, kata_baru):
        kata_baru = kata_baru.lower()

        if self.head is None:
            new_node = Node(kata_baru)
            self.head = new_node
            self.rear = new_node
            print(f"Kata pertama {kata_baru} berhasil ditambahkan")
            return True
        
        current = self.head
        while current:
            if current.kata == kata_baru:
                print("Kata sudah pernah dipakai sebelumnya, silakan coba kata lain")
                return False 
            current = current.next

        huruf_akhir = self.rear.kata[-1]
        huruf_awal = kata_baru[0]

        if huruf_akhir == huruf_awal:
            new_node = Node(kata_baru)
            self.rear.next = new_node
            self.rear = new_node
            print(f"kata '{kata_baru}' berhasil disambung")
            return True
        else:
            print(f"kata {kata_baru} tidak bisa disambung, huruf awal '{huruf_awal}' tidak sama dengan huruf akhir '{huruf_akhir}'")
            return False
        
    def tampilkan_rantai(self):
        if not self.head:
            print("rantai masih kosong")
            return
        
        current = self.head
        rantai = []
        while current:
            rantai.append(current.kata)
            current = current.next
        print("->".join(rantai))



game = RantaiKata()

print("GAME RANTAI KATA")
print("Ketik 'keluar' untuk berhenti, ketik 'mulai' untuk bermain")

while True:
    input_user = input("Masukkan kata: ").strip()
    
    if input_user.lower() == 'keluar':
        break
    elif input_user.lower() == 'mulai':
        game.tampilkan_rantai()
        continue

    if input_user:
        game.tambah_kata(input_user)

print("Game berakhir")
game.tampilkan_rantai()