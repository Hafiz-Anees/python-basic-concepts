'''
syntax:

lambda arguments:expression
'''

myinfo = lambda name,age: name + " ur rehman"

print(myinfo("anees",22))



# here is why we use lamda function
def calculator(n):
    return lambda  x:x*n

sum = calculator(2)
print(sum(3))


# lambda function can invoked immediately

(lambda :print("i am goog"))()



# lambda function with filter(funciton,iterable)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = list(filter(lambda x: x % 2 == 0, list1))

print(even_num)



# lambda function with map(funciton,iterable)

list2 = [2, 3, 4, 5]

newlist = list(map(lambda x: pow(x, 2), list2))

print(newlist)