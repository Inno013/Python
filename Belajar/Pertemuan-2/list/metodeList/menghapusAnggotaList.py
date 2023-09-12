# membuat list
my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']

# remove hanya menghapus elemen pertama yang dijumpai 
my_list.remove('p') 
print(my_list) 
my_list.remove('n') 
print(my_list)  
# pop akan menghapus anggota pada index dan 
# mengembalikan nilai yg terhapus
print(my_list.pop(1))
print(my_list)
# del akan menghapus anggota pada index
del my_list[2]
print(my_list)
# clear akan mengosongkan list
my_list.clear()
# # Output []
print(my_list)