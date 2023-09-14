my_list = ["I", "love","python","programming",2017] 
print(my_list[0]) 
print(my_list[2])
# list dalam list 
your_list = ["hello", [1,2,3, ["hello", "Nadus",[4,3]]], "python"] 
print(your_list[1][0]) 
print(your_list[1][2]) 
print(your_list[1][3][1][0])
print(your_list[1][-1][-2])
# IndexError 
# print(my_list[6])