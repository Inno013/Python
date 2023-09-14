# Definisi fungsi 
def print_info( nama = "Marvin", usia= 17 ): 
    """Fungsi ini menampilkan info yang dimasukkan""" 
    print ("Nama: ", nama) 
    print ("Usia ", usia) 
# Memanggil fungsi print_info 
print_info( usia = 29, nama = "Ancen" ) 
# Pemanggilan fungsi tidak menyediakan argumen usia 
print_info( nama = "Galih" )
print_info()