myinfo = """i am anees.
i am 22 years old.
i am studying computer science"""
print(myinfo)

# 1-indexing in string

print("character at index 45 is : ",myinfo[45])

# 2-slicing in string [start:end:increment]

print("my name is : ",myinfo[5:10])

# 3-reverse iteration 

name = "my name is anees"
n = len(name)
for i in range(n-1,0,-1):
  print(name[i])

#-----------------------------------------------------
print("\n-------------------------------------------------------\n")
  
myname = "my Name is anees"

print(myname.upper())

print(myname.title())

print(myname.lower())

print(myname.capitalize())

print(myname.find("anees")) # will return index no (-1 if not found)

print(myname.count('e')) # count the number of times 'e' appears in the string

print(myname.endswith("rehman"))  # checks whether a given substring is present at end or not

print("_".join(myname))

#----------------------------------------------------------
print("\n-------------------- IS ALPHA , IS DIGIT---------------------")

w="welcome"
print(w.isalpha())
print(w.isdigit())
print(w.isalnum())

print("\n-------------------------------------------------------\n")

# integer to character
c = chr(65)
print(c,type(c))

# character to integer

i = ord('A')
print(i,type(i))

#------------------------------------------------------------------------

print("\n-------------------STRING FORMATING------------------------------")

fullname1 = "my name is {fname} {lname}".format(fname="anees",lname ="rehman")
print(fullname1)

fullname2 = "my name is {0} {1}".format("anees","rehman")
print(fullname2)

fullname3 = "my name is {} {}".format("anees","rehman")
print(fullname3)



# --------------------------------------------------------------------------------------------------------------------

print("\n-------------------------------make translate and translate----------------------")

txt = "hello anees"
str1 = "anee"
str2 = "umer"

table = txt.maketrans(str1,str2)
print(table)
print(txt.translate(table))

# replace according to the ascii value in dicitonary 


#----------------------------------------------------------------------------------------

print("\n------------------------string to tuple-----------------------------------------")

food = "i can eat apple all day"

print(food.partition('apple'))


print("\n------------------------string to list------------------------------------------")

mylis = food.split()
print(mylis)


print("/n===============================================================================")

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print(food)
  print("price: %s" % prices[food])
  print("stock: %s" % stock[food])