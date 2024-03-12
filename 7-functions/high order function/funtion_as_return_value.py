print("\n=======================Function as a Return Value=======================\n")
def square(x):
    return x*x

def cube(x):
    return x*x*x

def mycalc(type):
    if type == 'square':
        return square
    else:
        return cube


result = mycalc('cube')

print(result(3))