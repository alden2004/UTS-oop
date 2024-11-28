class Rekening:
    # Atribut kelas
    nama_pemilik = ""
    saldo = 0.0

    def tampilkan_info(self):
        print(f"Nama Pemilik: {self.nama_pemilik}")
        print(f"Saldo: {self.saldo} IDR")

    def set_nama(self, nama):
        self.nama_pemilik = nama

    def set_saldo(self, saldo):
        self.saldo = saldo


def main():
    # Membuat objek Rekening
    rekening = Rekening()

    # Input dari pengguna
    rekening.set_nama(input("Masukkan nama pemilik rekening: "))
    rekening.set_saldo(float(input("Masukkan saldo rekening: ")))

    # Menampilkan informasi rekening
    rekening.tampilkan_info()


if __name__ == "__main__":
    main()