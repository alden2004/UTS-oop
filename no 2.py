class Mahasiswa:
    # Atribut kelas
    nama = ""
    umur = 0
    program_studi = ""
    nim = ""

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur}")
        print(f"Program Studi: {self.program_studi}")


def main():
    # Membuat objek Mahasiswa
    mahasiswa = Mahasiswa()

    # Input dari pengguna
    mahasiswa.nama = "Alden Muhammad Rafael"
    mahasiswa.nim = "202311001"
    mahasiswa.umur = int(input("Masukkan umur: "))
    mahasiswa.program_studi = "Informatika"

    # Menampilkan informasi mahasiswa
    mahasiswa.tampilkan_info()


if __name__ == "__main__":
    main()