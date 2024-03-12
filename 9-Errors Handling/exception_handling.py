
# ZeroDivisionError 

try:
    print(2/0)
except ZeroDivisionError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("zeroError code ended\n\n") 

# NameError (access variable or funciton without  defining them)
    
myname = "anees"

try:
    print(name)
except NameError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("NameError code ended\n\n") 


# TypeError : concatenating int and string : 'str' + int
    
num1 = 'q'
num2 = 2

try:
    print(num1+num2)
except TypeError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("TypeError code ended\n\n") 

# ValueError : I/O operation on closed file.

try:
    age =  int(input("enter age:"))
    print(age)
except ValueError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("ValueError code ended\n\n")  

# IndexError : list index out of range, tuple index out of range
    
numbers = [1,2,3,4,5]

try:
    print(numbers[7])
except IndexError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("IndexError code ended\n\n") 

# KeyError : 
    
booksList = {'name':'python','price':2000, 'author':'anees'}

try:
    print(booksList['name'])
    print(booksList['pages'])
except KeyError as error:
    print(f"Error : {error}")
else:
    print("successfully")
finally:
    print("keyError code ended\n\n") 

    
# ModuleNotFoundError : No module named 'xxx'

# ImportError : module is defined but accesing the function which is not defined in that module





