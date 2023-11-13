class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_pokok = 4000000
        self.uang_makan = 30000
        self.uang_transport = 0
        self.uang_tunjangan_profesi = 0
        self.uang_lembur = 0

    def absensi(self):
        print(f"{self.nama} melakukan absensi.")
        if self.jabatan == "Marketing":
            self.uang_makan += self.uang_makan

    def hitung_gaji(self):
        gaji_total = self.gaji_pokok + self.uang_makan + self.uang_transport + self.uang_tunjangan_profesi + self.uang_lembur
        print(f"\nGaji {self.nama} ({self.jabatan}): Rp {gaji_total}")


class Manager(Karyawan):
    def __init__(self, nama):
        super().__init__(nama, "Manager")
        self.uang_transport = 30
        self.uang_tunjangan_profesi = 1500000


class Admin(Karyawan):
    def __init__(self, nama):
        super().__init__(nama, "Admin")
        self.uang_transport = 15
        self.uang_lembur_per_jam = 40
        self.jam_lembur = 0

    def lembur(self, jam):
        print(f"{self.nama} bekerja lembur selama {jam} jam.")
        self.jam_lembur += jam
        self.uang_lembur = self.jam_lembur * self.uang_lembur_per_jam


class Marketing(Karyawan):
    def __init__(self, nama):
        super().__init__(nama, "Marketing")
        self.uang_transport = 50


# Contoh penggunaan
manager1 = Manager("John")
admin1 = Admin("Jane")
marketing1 = Marketing("Doe")

manager1.absensi()
manager1.hitung_gaji()

admin1.absensi()
admin1.lembur(2)  # Contoh lembur selama 2 jam
admin1.hitung_gaji()

marketing1.hitung_gaji()
