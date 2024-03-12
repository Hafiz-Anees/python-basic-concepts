# 6- reduce
l = [1,2,3,4]
from functools import reduce
sum = lambda a,b:a+b

value = reduce(sum,l)
print(value)