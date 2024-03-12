# 5- filter function

def greater(n):
  if n>5:
    return True
  else:
    return False
n1 = list(filter(lambda x:x>5,[1,2,6,7,8]))
n2 = list(filter(greater,[1,2,6,7,8]))
print(n1)
print(n2)