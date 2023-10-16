class Orang():
    def __init__(self, firstName, LastName):
        self.firstName = firstName
        self.LastName = LastName

    def getfirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.LastName
    
class Alamat():
    def __init__(self, jalan, kota):
        self.jalan = jalan
        self.kota = kota

class Mahasiswa(Orang,Alamat) :
        def __init__(self, firstName, LastName, nim, jalan, kota):
          self.nim = nim

          Orang.__init__(self, firstName, LastName)
          Alamat.__init__(self, jalan, kota)

        def __str__(self):
          return f"{self.firstName} {self.LastName} {self.nim}"
        
        def printData(self):
            print(f"Nama: {self.getfirstName()} {self.LastName}")
            print(f"NIM: {self.nim}")
            print(f"Alamat: {self.jalan}, {self.kota}")

mhs = Mahasiswa("Deni","wildan", "2207023", "cibatu", "Garut")
mhs.printData()