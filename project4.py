class Tugas:
    def __init__(self,BangunDatar):
       self.BangunDatar = BangunDatar
  

import math

class Persegi(Tugas):
    def __init__(self, sisi, BangunDatar):
        self.sisi = sisi
        super().__init__(BangunDatar)

    def luas(self):
        return self.sisi*self.sisi
    
    def hasilakhir(self):
        print(f"Aku adalah {self.BangunDatar}")
        print(f"luas {self.BangunDatar} dengan sisi {self.sisi} adalah {self.luas()}")

class Lingkaran(Tugas):
    def __init__(self, jarijari, BangunDatar):
        self.jarijari = jarijari
        super().__init__(BangunDatar)

    def luas(self):
        return math.pi * self.jarijari**2
    
    def hasilakhir(self):
        print(f"Aku adalah {self.BangunDatar}")
        print(f"luas {self.BangunDatar} dengan jari jari {self.jarijari} adalah {self.luas()}")

persegi = Persegi(4, "persegi")
persegi.hasilakhir()
lingkaran = Lingkaran(7, "lingkaran")
lingkaran.hasilakhir()