class Laptop:
    # Atribut kelas
    merk = ""
    ram = 0
    penyimpanan = 0

    def tampilkan_info(self):
        print(f"Merek: {self.merk}")
        print(f"RAM: {self.ram} GB")
        print(f"Penyimpanan: {self.penyimpanan} GB")


def main():
    # Membuat objek Laptop
    laptop = Laptop()

    # Input dari pengguna
    laptop.merk = input("Masukkan merek laptop: ")
    laptop.ram = int(input("Masukkan kapasitas RAM (dalam GB): "))
    laptop.penyimpanan = int(input("Masukkan kapasitas penyimpanan (dalam GB): "))

    # Menampilkan informasi laptop
    laptop.tampilkan_info()


if __name__ == "__main__":
    main()