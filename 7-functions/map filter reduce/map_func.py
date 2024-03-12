# 4-map function  === apply on each item of the list
def square(x):
  return x*x
l = [1,2,3,4]
# n = list(map(lambda x:x*x,l))
n = list(map(square,l))
print(n)