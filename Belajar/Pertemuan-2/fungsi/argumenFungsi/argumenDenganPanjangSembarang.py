# Definisi fungsi 
def print_info( arg1, *vartuple ): 
    """Fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan""" 
    print ("Outputnya adalah: ") 
    print (arg1) 
    my_list = list(vartuple)
    print(my_list)
    # for i in vartuple: 
    #     print (i) 

# Pemanggilan fungsi 
# Satu argumen 
print_info( 10 ) 
#my_list = [6,8,9,4]
# Empat argumen 
print_info( 10, 9,8,7,5,4 )