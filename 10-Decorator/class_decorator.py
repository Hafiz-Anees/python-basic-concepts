class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed")
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
  print("dislay function ran")

display()

print("\n===================================\n")

@decorator_class
def display_info(name, age):
    print("{}, {}".format(name, age))

display_info("musa",32)