class SlotState:
    EMPTY = 0
    OCCUPIED = 1


class AkunPlayer:
    def __init__(self):
        self.player_id = None
        self.username = None
        self.state = SlotState.EMPTY


class HashMapAkunGame:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [AkunPlayer() for _ in range(self.SIZE)]

    def hash_function(self, player_id):
        return (player_id % self.SIZE + self.SIZE) % self.SIZE

    def akun_pemain(self, player_id, username):
        idx = self.hash_function(player_id)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].player_id == player_id:
                    self.table[i].username = username
                    return True

            else:
                self.table[i].player_id = player_id
                self.table[i].username = username
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def cari_akun(self, player_id):
        idx = self.hash_function(player_id)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].player_id == player_id):
                return self.table[i]

        return None

    def tampilkan_data(self):
        print("\n=== DATA AKUN GAME RPG ===")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            else:
                print(
                    f"Player ID: {self.table[i].player_id}, "
                    f"Username: {self.table[i].username}"
                )


def main():
    game = HashMapAkunGame()

    game.akun_pemain(1001, "ShadowHunter")
    game.akun_pemain(1011, "DarkMage")
    game.akun_pemain(1021, "HolyKnight")
    game.akun_pemain(1031, "ElfArcher")

    print("===== LOGIN GAME RPG =====")

    while True:
        player_id = int(input("Masukkan Player ID: "))

        akun = game.cari_akun(player_id)

        if akun is not None:
            print("\n=== LOGIN BERHASIL ===")
            print(f"Selamat datang, {akun.username}, Selamat bermain!")
            break

        else:
            print("\n=== LOGIN GAGAL ===")
            print("Player ID tidak ditemukan. Silakan coba lagi.")


if __name__ == "__main__":
    main()