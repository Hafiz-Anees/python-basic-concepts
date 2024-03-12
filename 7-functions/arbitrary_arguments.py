
'''
arbitrary arguement use when we don;t know the exact numbers of arguments will pass to function
'''

# * make tuple (arbitraray argument)
def my_function(*num):
    print(num,type(num))

my_function(1, 2, 3, 'a', 'b')

my_function("anees","umer","qasim")


# ** make dictionary  (arbitrary keyword arguement)
def print_names(**names):
    print(names,type(names))
    print(names['n1'])

print_names(n1="anees",n2="umer",n3="ikram",n4= "qasim")