"""
decorator is same as closure function but instead they accept function
as an argument

"""

def decorator_function(original_function):
  def wrapper_function(*args,**kwargs):
    print("our wrpper function executed this before: {}".format(original_function.__name__))
    return original_function(*args,**kwargs)
  return wrapper_function

@decorator_function  # explained below 
def display():
  print('display function ran')

display()

# explanation of @decorator_function
# decoarted_display = decorator_function(display)
# decoarted_display()

print("\n===================================\n")
@decorator_function
def display_info(name,age):
  print("{},{}".format(name,age))

display_info("anees",22)