# misal ada nilai yang salah 
ganjil = [1,3,4,7,9] 
# ubah item ke 3 (indeks ke 2) 
ganjil[2] = 5
print(ganjil) 
# mengubah sekali banyak 
ganjil[2:5] = [11,13,15] 
print(ganjil)

nim = "682022238"
prodi = nim[0:2]
angkatan = nim[2:6]

if(prodi == "67"):
    print("Mahasiswa prodi S1 TI")
elif(prodi == "68"):
    print("Mahasiswa prodi S1 SI")
if(angkatan == "2021"):
    print("Mahasiswa angkatan 2021")
elif(angkatan == "2022"):
    print("Mahasiswa angkatan 2022")