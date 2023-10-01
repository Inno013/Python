# import class Karyawan
from pembuatanClass import Karyawan

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000)

# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000)

# Mengakses Attribute Object
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)