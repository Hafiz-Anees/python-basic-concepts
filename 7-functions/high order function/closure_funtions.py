"""
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure

"""

# example 1

def outer_func():
  message = 'this is outer function'

  def inner_func():
    print(message)

  return inner_func()

outer_func()

#--------------------------------------------------

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20