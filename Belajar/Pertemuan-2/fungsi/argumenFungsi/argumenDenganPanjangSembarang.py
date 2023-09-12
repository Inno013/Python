# Definisi fungsi 
def print_info( arg1, *vartuple ): 
    """Fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan""" 
    print ("Outputnya adalah: ") 
    print (arg1) 
    for var in vartuple: 
        print (var) 

# Pemanggilan fungsi 
# Satu argumen 
print_info( 10 ) 

# Empat argumen 
print_info( 10, 30, 50, 70 )