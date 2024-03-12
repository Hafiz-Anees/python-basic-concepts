# First class Function (High Order Function)

"""
1-->this mean we can assign function to a variable
2-->can be pass an argument to another function
3-->can be return from the body of another funciton

"""


def square(x):
    return x*x

f = square     # assigning function to variable
print(f(5))

def my_map(func,arg):
  result = []
  for i in arg:
    result.append(func(i))
  return result

squares  = my_map(square,[1,2,3])  # passing function as an argument

print(squares)


# return function from another funtion

def logger(msg):
  def log_message():
    print("log:",msg)

  return log_message

log_hi = logger("HI")
log_hi()

#-------------------------------------------------

def html_tag(tag):
  def message(msg):
    print("<{0}>{1}</{0}>".format(tag,msg))
  
  return message

h1 = html_tag("h1")
h1("this is heading")

