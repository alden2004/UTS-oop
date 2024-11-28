class AkunBank:
    # Atribut kelas
    nama_pemilik = ""
    saldo = 0.0

    def set_nama(self, nama):
        self.nama_pemilik = nama

    def set_saldo(self, saldo):
        self.saldo = saldo

    def tambah_saldo(self, jumlah):
        self.saldo += jumlah

    def tampilkan_info(self):
        print(f"Nama Pemilik: {self.nama_pemilik}")
        print(f"Saldo: {self.saldo} IDR")


class Hewan:
    suara = ""

    def set_suara(self, suara):
        self.suara = suara

    def buat_suara(self):
        return self.suara


class Anjing(Hewan):
    def buat_suara(self):
        return "Guk Guk"  # Method overriding


def main():
    # Membuat objek AkunBank
    akun = AkunBank()
    akun.set_nama("Alden")
    akun.set_saldo(100000)

    # Menampilkan informasi akun bank
    akun.tampilkan_info()

    # Membuat objek Anjing
    anjing = Anjing()
    anjing.set_suara("Guk Guk")

    # Menampilkan suara anjing
    print(f"Suara Anjing: {anjing.buat_suara()}")


if __name__ == "__main__":
    main()