# contoh penggunaan duck typing
def print_all(items):
    for item in items:
        print(item)

# list
my_list = [1, 2, 3]

# tuple
my_tuple = (4, 5, 6)

# string
my_string = "Hello, world!"

# memanggil fungsi print_all dengan parameter my_list, my_tuple, dan my_string
print_all(my_list) # output: 1 2 3
print_all(my_tuple) # output: 4 5 6
print_all(my_string) # output: H e l l o , w o r l d !
