t = ("python")  # this is not a tuple bcs it has only one value
print(type (t))

t1 = (1,2,3,4,5,6,6,7)
print(sum(t1))
print(sum(t1,12))
print("maxumu : ",max(t1))
print("minimum: ",min(t1))
print(t1.count(6))

print("length : ", len(t1))



numbers = (1,2,3,4,5,6,7,8,9)

n1,n2,n3,*remainig = numbers
print(n1)
print(n2)
print(remainig)